#Actual complete helper functions that are complete and not to show in the website
#If you are a student reading this:
# 1) Congrats.
# 2) Still write the functions yourself, don't be lazy you won't have github access during
# the exam. (And neither chatGPT)
import itertools
import numpy as np
import sympy as sp


def lambda_mu(E,nu):
    """Convert linear elastic constant parameters from E,nu to lambda, mu

    Args:
        E : Young's modulus
        nu : Poisson ratio

    Returns:
        (lambda,mu): The Lamé constants parameters.
    """    
    lam = nu * E / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    return lam,mu


def E_nu(lam, mu):
    """Convert linear elastic constant parameters from lambda, mu to E, nu

    Args:
        lam : First Lamé parameter
        mu : Second Lamé parameter (shear modulus)

    Returns:
        (E, nu): Young's modulus and Poisson ratio.
    """
    E = mu * (3 * lam + 2 * mu) / (lam + mu)
    nu = lam / (2 * (lam + mu))
    return E, nu


def is_sympy_array(S):
    return isinstance(S, sp.MatrixBase)

def vol(S):
    """
    Volumetric (spherical) part of a second order tensor.
    vol(S) = mean(S) * I, where mean(S) = tr(S)/3.
    """
    n = S.shape[0]
    if is_sympy_array(S):
        trace = S.trace() / 3
        return trace * sp.eye(n)
    else:
        trace = np.trace(S) / 3.0
        return trace * np.eye(n)

def dev(S):
    """
    Deviatoric part of a second order tensor (additive decomposition).
    dev(S) = S - vol(S), traceless by construction.
    """
    return S - vol(S)

def check_symmetry(A, tol=1e-10):
    """
    Raise an error if matrix A is not symmetric.

    Parameters
    ----------
    A : array-like or sympy Matrix, shape (n,n)
    tol : float
        Tolerance for numeric comparisons (ignored for symbolic input,
        where equality must hold exactly after simplification).
    """
    symbolic = is_sympy_array(A)

    if symbolic:
        diff = sp.simplify(A - A.T)
        if not diff.is_zero_matrix:
            raise ValueError("Matrix is not symmetric")
    else:
        A = np.asarray(A)
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix is not square")
        if not np.allclose(A, A.T, atol=tol):
            raise ValueError("Matrix is not symmetric")

def to_voigt(eps_or_sigma, mode="strain"):
    """
    Convert a symmetric second-order tensor (2x2 or 3x3) to Voigt notation.

    Parameters
    ----------
    eps_or_sigma : array-like or sympy Matrix, shape (2,2) or (3,3)
        Strain or stress tensor.
    mode : str
        "strain" -> off-diagonal terms multiplied by 2 (engineering shear strain)
        "stress" -> off-diagonal terms unchanged

    Returns
    -------
    Voigt vector:
        3x3 input -> shape (6,): [11, 22, 33, 23, 13, 12]
        2x2 input -> shape (3,): [11, 22, 12]
    """
    check_symmetry(eps_or_sigma)
    symbolic = is_sympy_array(eps_or_sigma)
    dim = eps_or_sigma.shape[0]

    if mode == "strain":
        n = 2
    elif mode == "stress":
        n = 1
    else:
        raise ValueError('Unknown mode. Allowed modes are "stress" and "strain"')

    if dim == 3:
        voigt = sp.zeros(6, 1) if symbolic else np.zeros(6)
        voigt[0] = eps_or_sigma[0, 0]
        voigt[1] = eps_or_sigma[1, 1]
        voigt[2] = eps_or_sigma[2, 2]
        voigt[3] = eps_or_sigma[1, 2] * n
        voigt[4] = eps_or_sigma[0, 2] * n
        voigt[5] = eps_or_sigma[0, 1] * n
    elif dim == 2:
        voigt = sp.zeros(3, 1) if symbolic else np.zeros(3)
        voigt[0] = eps_or_sigma[0, 0]
        voigt[1] = eps_or_sigma[1, 1]
        voigt[2] = eps_or_sigma[0, 1] * n
    else:
        raise ValueError("Input must be a 2x2 or 3x3 tensor")

    return voigt

def from_voigt(voigt, mode="strain"):
    """
    Convert a Voigt-notation vector back to a symmetric second-order tensor.

    Parameters
    ----------
    voigt : array-like or sympy Matrix, length 3 or 6
        length 6 -> [11, 22, 33, 23, 13, 12] -> returns 3x3 tensor
        length 3 -> [11, 22, 12]             -> returns 2x2 tensor
    mode : str
        "strain" -> off-diagonal voigt terms divided by 2 (undo engineering shear strain)
        "stress" -> off-diagonal voigt terms unchanged

    Returns
    -------
    Symmetric tensor, shape (2,2) or (3,3)
    """
    symbolic = is_sympy_array(voigt)
    n_entries = voigt.shape[0] if hasattr(voigt, "shape") else len(voigt)

    if mode == "strain":
        n = 2
    elif mode == "stress":
        n = 1
    else:
        raise ValueError('Unknown mode. Allowed modes are "stress" and "strain"')

    if n_entries == 6:
        T = sp.zeros(3, 3) if symbolic else np.zeros((3, 3))
        T[0, 0] = voigt[0]
        T[1, 1] = voigt[1]
        T[2, 2] = voigt[2]
        T[1, 2] = T[2, 1] = voigt[3] / n
        T[0, 2] = T[2, 0] = voigt[4] / n
        T[0, 1] = T[1, 0] = voigt[5] / n
    elif n_entries == 3:
        T = sp.zeros(2, 2) if symbolic else np.zeros((2, 2))
        T[0, 0] = voigt[0]
        T[1, 1] = voigt[1]
        T[0, 1] = T[1, 0] = voigt[2] / n
    else:
        raise ValueError("Input must have length 3 or 6")

    return T

def stiffness_matrix_voigt(lam, mu) -> np.ndarray:
    """
    Isotropic stiffness matrix C_iso in Voigt notation (6x6), engineering shear strain convention.
    sigma = C_iso @ [e11, e22, e33, 2e23, 2e13, 2e12]
    Automatically uses sympy if lam or mu is a sympy expression, else numpy.
    """
    symbolic = isinstance(lam, sp.Basic) or isinstance(mu, sp.Basic)
    C = sp.zeros(6, 6) if symbolic else np.zeros((6, 6))

    C[0, 0] = C[1, 1] = C[2, 2] = 2 * mu + lam
    C[0, 1] = C[0, 2] = C[1, 0] = C[1, 2] = C[2, 0] = C[2, 1] = lam
    C[3, 3] = C[4, 4] = C[5, 5] = mu
    return C

def compliance_matrix_voigt(E, nu) -> np.ndarray:
    """
    Isotropic compliance matrix S_iso in Voigt notation (6x6), engineering shear strain convention.
    [e11, e22, e33, 2e23, 2e13, 2e12] = S_iso @ sigma
    Automatically uses sympy if E or nu is a sympy expression, else numpy.
    """
    symbolic = isinstance(E, sp.Basic) or isinstance(nu, sp.Basic)
    S = sp.zeros(6, 6) if symbolic else np.zeros((6, 6))

    S[0, 0] = S[1, 1] = S[2, 2] = 1
    S[0, 1] = S[0, 2] = S[1, 0] = S[1, 2] = S[2, 0] = S[2, 1] = -nu
    S[3, 3] = S[4, 4] = S[5, 5] = 2 * (1 + nu)

    S = S / E

    return S

