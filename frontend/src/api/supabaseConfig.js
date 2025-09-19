import { createClient } from '@supabase/supabase-js';

// The supabaseConfig.js file contains the configuration and utility functions for Supabase.
// It provides methods for interacting with Supabase Storage and generating public URLs.

// Initialize Supabase client
const supabaseUrl = process.env.REACT_APP_SUPABASE_URL;
const supabaseKey = process.env.REACT_APP_SUPABASE_KEY;
export const supabase = createClient(supabaseUrl, supabaseKey);

// Function to upload an image to Supabase Storage
// This function uploads a file to the specified bucket and returns the upload data.
export const uploadImage = async (bucketName, filePath, file) => {
  const { data, error } = await supabase.storage.from(bucketName).upload(filePath, file);
  if (error) {
    throw new Error(`Image upload failed: ${error.message}`);
  }
  return data;
};

// Function to get a public URL for an image
// This function retrieves the public URL of a file stored in Supabase Storage.
export const getImageUrl = (bucketName, filePath) => {
  const { data } = supabase.storage.from(bucketName).getPublicUrl(filePath);
  return data?.publicUrl || "";
};