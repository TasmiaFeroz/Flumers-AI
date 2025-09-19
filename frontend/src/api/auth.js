import { auth } from "./firebaseConfig";
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  signOut,
} from "firebase/auth";

// The auth.js file contains functions for user authentication using Firebase.
// It provides methods for Google login, email/password login, and user sign-out.

// Google Login
// This function allows users to sign in using their Google account.
export const loginWithGoogle = async () => {
  const provider = new GoogleAuthProvider();
  try {
    const result = await signInWithPopup(auth, provider);
    // Return the authenticated user object
    return result.user;
  } catch (error) {
    // Throw an error if the login fails
    throw new Error(error.message);
  }
};

// Email/Password Login
// This function allows users to sign in using their email and password.
export const loginWithEmail = async (email, password) => {
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    // Return the authenticated user object
    return userCredential.user;
  } catch (error) {
    // Throw an error if the login fails
    throw new Error(error.message);
  }
};

// Email/Password Signup
// This function allows new users to create an account using their email and password.
export const signupWithEmail = async (email, password) => {
  try {
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    // Return the newly created user object
    return userCredential.user;
  } catch (error) {
    // Throw an error if the signup fails
    throw new Error(error.message);
  }
};

// Logout
// This function allows users to sign out from their account.
export const logout = async () => {
  try {
    await signOut(auth);
  } catch (error) {
    // Throw an error if the logout fails
    throw new Error(error.message);
  }
};