import pydicom
import numpy as np
import cv2

# Create a synthetic image and save as a DICOM file
def create_synthetic_dicom(output_filename):
    try:
        # Create a blank image with shapes
        image = np.zeros((256, 256), dtype=np.uint16)  # DICOM typically uses uint16 for pixel values

        # Draw some shapes
        cv2.circle(image, (80, 80), 30, (255), -1)  # Object 1
        cv2.rectangle(image, (120, 50), (200, 150), (255), -1)  # Object 2
        cv2.circle(image, (180, 200), 40, (255), -1)  # Object 3
        cv2.rectangle(image, (10, 150), (70, 230), (255), -1)  # Object 4

        # Create a DICOM dataset
        ds = pydicom.Dataset()
        ds.PatientName = "Test^Patient"
        ds.PatientID = "123456"
        ds.Modality = "OT"  # Other
        ds.Rows, ds.Columns = image.shape
        ds.PixelData = image.tobytes()
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.BitsAllocated = 16
        ds.BitsStored = 16
        ds.HighBit = 15
        ds.PixelRepresentation = 0  # Unsigned integer

        # Set required attributes
        ds.is_little_endian = True  # Set byte order
        ds.is_implicit_VR = True     # Set value representation to implicit

        # Save the DICOM file
        pydicom.dcmwrite(output_filename, ds)
        print(f"DICOM file saved as {output_filename}")

    except Exception as e:
        print(f"An error occurred while creating the DICOM file: {e}")

# Example usage
output_filename = "D:/geometri.dcm"  # Change this path if needed
create_synthetic_dicom(output_filename)
