import moviepy.editor as mp
import os

def convert_video_to_audio(video_path, output_path=None):
    try:
        # Step 1: Convert Video (load the video)
        print("Loading video...")
        video = mp.VideoFileClip(video_path)
        
        # Step 2 & 3: Decode MP4 and Extract Audio
        print("Extracting audio...")
        audio = video.audio
        
        # Generate output path if not provided
        if output_path is None:
            output_path = os.path.splitext(video_path)[0] + '.mp3'
        
        # Step 4: Encode MP3
        print("Converting to MP3...")
        audio.write_audiofile(output_path)
        
        # Step 5: Conversion Completed
        print("Conversion completed successfully!")
        
        # Clean up
        video.close()
        audio.close()
        
        return True, output_path
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False, None

def main():
    while True:
        video_path = input("Enter the path to your MP4 video (or 'q' to quit): ")
        
        if video_path.lower() == 'q':
            break
        
        if not os.path.exists(video_path):
            print("File does not exist. Please try again.")
            continue
            
        success, output_path = convert_video_to_audio(video_path)
        
        if success:
            print(f"Audio saved as: {output_path}")
        
        print("\n")

if __name__ == "__main__":
    main()
