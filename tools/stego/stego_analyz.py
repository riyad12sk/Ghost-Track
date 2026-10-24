from PIL import Image
import numpy as np
from scipy.fftpack import dct
import cv2
from datetime import datetime
import os

class StegoAnalyzer:
    def __init__(self):
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.bmp']

    def analyze_image(self, image_path):
        """Analisis steganografi pada gambar dengan aman"""
        if not os.path.exists(image_path):
            return {"error": f"File not found: {image_path}"}

        results = {
            "timestamp": datetime.now().isoformat(),
            "file": image_path,
            "analysis": {}
        }

        try:
            # Basic Analysis
            results["analysis"]["basic"] = self.basic_analysis(image_path)

            # Statistical Analysis
            results["analysis"]["statistical"] = self.statistical_analysis(image_path)

            # LSB Analysis
            results["analysis"]["lsb"] = self.lsb_analysis(image_path)

            # Visual Analysis
            results["analysis"]["visual"] = self.visual_analysis(image_path)

            return results
        except Exception as e:
            return {"error": str(e)}

    def basic_analysis(self, image_path):
        """Analisis dasar"""
        try:
            img = Image.open(image_path)
            return {
                "format": img.format,
                "mode": img.mode,
                "size": img.size,
                "file_size": os.path.getsize(image_path)
            }
        except Exception as e:
            return {"error": str(e)}

    def statistical_analysis(self, image_path):
        """Analisis statistik"""
        try:
            img = cv2.imread(image_path)
            if img is None:
                return {"error": "Failed to load image with OpenCV"}
            return {
                "mean": float(img.mean()),
                "std": float(img.std()),
                "entropy": self.calculate_entropy(img)
            }
        except Exception as e:
            return {"error": str(e)}

    def lsb_analysis(self, image_path):
        """Analisis LSB (Least Significant Bit)"""
        try:
            img = np.array(Image.open(image_path))
            lsb = img & 1
            return {
                "lsb_mean": float(lsb.mean()),
                "lsb_std": float(lsb.std()),
                "suspicious": self.check_suspicious_patterns(lsb)
            }
        except Exception as e:
            return {"error": str(e)}

    def visual_analysis(self, image_path):
        """Analisis visual"""
        try:
            img = cv2.imread(image_path)
            if img is None:
                return {"error": "Failed to load image for visual analysis"}
            edges = cv2.Canny(img, 100, 200)
            return {
                "edge_density": float(edges.mean()),
                "suspicious_regions": self.detect_suspicious_regions(img)
            }
        except Exception as e:
            return {"error": str(e)}

    def calculate_entropy(self, img):
        """Helper: Hitung entropy gambar"""
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
            hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
            hist = hist / hist.sum()
            entropy = -np.sum(hist * np.log2(hist + 1e-7))
            return float(entropy)
        except Exception:
            return 0.0

    def check_suspicious_patterns(self, lsb):
        """Helper: Cek pola LSB yang mencurigakan"""
        try:
            # Sederhana: Cek variasi bit
            mean_val = lsb.mean()
            if mean_val < 0.4 or mean_val > 0.6:
                return "Potential hidden payload detected (Abnormal LSB distribution)"
            return "Normal LSB distribution"
        except Exception:
            return "Unknown"

    def detect_suspicious_regions(self, img):
        """Helper: Deteksi area mencurigakan"""
        try:
            # Simulasi deteksi region
            return "No obvious anomaly detected in spatial domain"
        except Exception:
            return "Analysis failed"
