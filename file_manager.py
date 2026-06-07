import os
import shutil

def automate_folder_cleanup():
    print("📂 Nexus Automation: Starting folder optimization script...")
    
    # Define the target directory (Current directory where the script runs)
    current_directory = os.getcwd()
    
    # Target folders for organization
    image_folder = os.path.join(current_directory, "Organized_Images")
    document_folder = os.path.join(current_directory, "Organized_Documents")
    
    # Track moved files count
    moved_images = 0
    moved_docs = 0

    # Extensions to track
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    doc_extensions = ['.txt', '.pdf', '.docx', '.xlsx']

    # Scan and sort files
    for filename in os.listdir(current_directory):
        file_path = os.path.join(current_directory, filename)
        
        # FIXED: Added 'README.md' to the skip list so it stays safe!
        if os.path.isdir(file_path) or filename in ['file_manager.py', 'chatbot.py', 'README.md']:
            continue
            
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Move Images
        if file_extension in image_extensions:
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)
            shutil.move(file_path, os.path.join(image_folder, filename))
            moved_images += 1
            print(f"Moved Image: {filename}")
            
        # Move Documents
        elif file_extension in doc_extensions:
            if not os.path.exists(document_folder):
                os.makedirs(document_folder)
            shutil.move(file_path, os.path.join(document_folder, filename))
            moved_docs += 1
            print(f"Moved Document: {filename}")

    print("\n📊 Run Summary:")
    print(f"✅ Images organized: {moved_images}")
    print(f"✅ Documents organized: {moved_docs}")
    print("🎉 Folder cleanup complete!")

if __name__ == "__main__":
    automate_folder_cleanup()
