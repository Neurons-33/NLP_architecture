import io
import cloudinary.uploader
import datetime


def upload_pil_image(image, folder="generated_cards"):

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    filename = datetime.datetime.now().strftime("card_%Y%m%d_%H%M%S")

    result = cloudinary.uploader.upload(
        buffer,
        folder=folder,
        public_id=filename,
        resource_type="image"
    )

    return {
        "secure_url": result["secure_url"],
        "public_id": result["public_id"]
    }