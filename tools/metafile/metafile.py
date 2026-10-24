import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# লাইব্রেরি সেফ ইমপোর্ট (যদি ইনস্টল না থাকে যাতে ক্র্যাশ না করে)
try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False


class MetadataExtractor:
    def __init__(self):
        self.supported_types = {
            'image': ['.jpg', '.jpeg', '.png', '.tiff', '.bmp'],
            'document': ['.pdf', '.doc', '.docx'],
            'audio': ['.mp3', '.wav'],
            'video': ['.mp4', '.avi']
        }

    def extract_metadata(self, file_path):
        """Extract metadata dari file dengan aman"""
        file_path = str(file_path).strip()
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}

        try:
            # ফাইল টাইপ ডিটেক্ট করা (সেফলি)
            file_type = "unknown/unknown"
            if MAGIC_AVAILABLE:
                try:
                    file_type = magic.from_file(file_path, mime=True)
                except Exception:
                    pass

            ext = os.path.splitext(file_path)[1].lower()

            results = {
                "timestamp": datetime.now().isoformat(),
                "file_path": file_path,
                "file_type": file_type,
                "file_size": os.path.getsize(file_path),
                "metadata": {}
            }

            if ext in self.supported_types['image']:
                results["metadata"] = self.extract_image_metadata(file_path)
            elif ext in self.supported_types['document']:
                results["metadata"] = self.extract_document_metadata(file_path)
            else:
                results["metadata"] = {"info": "Basic file attributes extracted (Specific metadata parser not available for this format)"}

            return results
        except Exception as e:
            return {"error": str(e)}

    def extract_image_metadata(self, image_path):
        """Extract metadata dari gambar dengan aman"""
        try:
            with Image.open(image_path) as image:
                exif = {}
                if hasattr(image, '_getexif'):
                    info = image._getexif()
                    if info:
                        for tag, value in info.items():
                            decoded = TAGS.get(tag, tag)
                            # ডাটা কনভার্শন যাতে JSON সেরিলাইজেশনে সমস্যা না হয়
                            exif[str(decoded)] = str(value)

                return {
                    "format": image.format,
                    "mode": image.mode,
                    "size": image.size,
                    "exif": exif
                }
        except Exception as e:
            return {"error": f"Image metadata extraction failed: {str(e)}"}

    def extract_document_metadata(self, doc_path):
        """Extract metadata dari dokumen dengan aman"""
        try:
            if doc_path.lower().endswith('.pdf'):
                if not PDF_AVAILABLE:
                    return {"error": "PyPDF2 module not installed"}

                with open(doc_path, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    info = pdf.metadata
                    
                    # সেফলি মেডডাটা রিড করা
                    author = info.get('/Author', '') if info else ''
                    creator = info.get('/Creator', '') if info else ''
                    producer = info.get('/Producer', '') if info else ''
                    subject = info.get('/Subject', '') if info else ''
                    title = info.get('/Title', '') if info else ''

                    return {
                        "author": str(author) if author else "Unknown",
                        "creator": str(creator) if creator else "Unknown",
                        "producer": str(producer) if producer else "Unknown",
                        "subject": str(subject) if subject else "Unknown",
                        "title": str(title) if title else "Unknown",
                        "pages": len(pdf.pages) if pdf.pages else 0
                    }
            return {"error": "Unsupported document format or non-PDF file"}
        except Exception as e:
            return {"error": f"Document metadata extraction failed: {str(e)}"}
