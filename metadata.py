import ffmpeg

def extract_metadata(video_path):
    probe = ffmpeg.probe(video_path)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    metadata = {
        'codec': video_info['codec_name'],
        'resolution': f"{video_info['width']}x{video_info['height']}",
        'frame_rate': eval(video_info['r_frame_rate']),
        'duration': float(video_info['duration']),
    }
    return metadata

# Quick test:
if __name__ == "__main__":
    print(extract_metadata("samples/small_test.mp4"))
