import pydicom
import matplotlib.pyplot as plt

# Load X-ray DICOM file
ds = pydicom.dcmread("xray/IM-0003-0001.dcm")
img = ds.pixel_array

# Display raw X-ray image
plt.figure(figsize=(6,6))
plt.imshow(img, cmap="gray")
plt.title("Raw X-ray - A8")
plt.axis("off")
plt.savefig("xray_raw_A8.png", dpi=300, bbox_inches="tight")
plt.show()
