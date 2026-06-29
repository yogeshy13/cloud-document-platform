from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile


class StorageService:

    def __init__(self):

        self.upload_dir = Path("uploads")

        self.upload_dir.mkdir(
            exist_ok=True
        )

    def save_file(
        self,
        file: UploadFile,
    ) -> str:

        extension = Path(file.filename).suffix

        stored_filename = (
            f"{uuid4()}{extension}"
        )

        destination = (
            self.upload_dir / stored_filename
        )

        with destination.open("wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return stored_filename

    def delete_file(
        self,
        stored_filename: str,
    ):

        file_path = (
            self.upload_dir / stored_filename
        )

        if file_path.exists():
            file_path.unlink()

    def get_file_path(
        self,
        stored_filename: str,
    ) -> Path:

        return (
            self.upload_dir / stored_filename
        )