<?php
// Set a base directory where all project folders will be created.
// This should be outside the web root for security. For this example,
// we will assume it's a "uploads" folder in the same directory as this script.
$base_upload_dir = 'uploads/';

// --- Form Validation and Data Retrieval ---
// Check if the form was submitted via POST
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    die("Invalid request method.");
}

// Check for required fields: student number, project name, and file
if (empty($_POST["student_number"]) || empty($_POST["project_name"]) || empty($_FILES["uploaded_file"]["name"])) {
    die("Upload failed. Make sure the filesize is less than 10MB.");
}

// Sanitize the student number to ensure it's a valid integer
$student_number = filter_var($_POST["student_number"], FILTER_SANITIZE_NUMBER_INT);
// Add an additional check to ensure it contains only digits
if (!preg_match("/^[0-9]+$/", $student_number)) {
    die("Invalid student number. Please use only digits.");
}

$project_name = $_POST["project_name"];
$file_info = $_FILES["uploaded_file"];

// Validate the uploaded file for potential errors
if ($file_info["error"] !== UPLOAD_ERR_OK) {
    die("File upload failed with error code: " . $file_info["error"]);
}

// --- Directory and File Naming Logic ---
// Map the selected project name to a specific directory name
$project_directories = [
    'Project1' => 'project1_files/',
    'Project2' => 'project2_files/',
    'Project3' => 'project3_files/',
    'Project4' => 'project4_files/',
];

// Determine the target directory based on the project name
if (!isset($project_directories[$project_name])) {
    die("Invalid project selected.");
}

$target_directory = $base_upload_dir . $project_directories[$project_name];

// Get the file extension from the original filename
$file_extension = pathinfo($file_info["name"], PATHINFO_EXTENSION);

// Construct the new filename using the student number
$new_file_name = $student_number . '.' . $file_extension;
$target_file_path = $target_directory . $new_file_name;

// --- Server-Side File Handling ---
// Create the target directory if it doesn't exist
if (!is_dir($target_directory)) {
    // The 'true' parameter allows for recursive directory creation
    if (!mkdir($target_directory, 0755, true)) {
        die("Failed to create directory: " . $target_directory);
    }
}

// Move the uploaded file to its new location with the new name
if (move_uploaded_file($file_info["tmp_name"], $target_file_path)) {
    echo "File " . htmlspecialchars($new_file_name) . " has been uploaded successfully to " . htmlspecialchars($target_directory) . ".";
} else {
    echo "Sorry, there was an error uploading your file.";
}
?>

