from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import StorageService


class DocumentService:

    def __init__(self, db: Session):
        self.repo = DocumentRepository(db)
        self.storage = StorageService()

    def upload_document(
        self,
        file: UploadFile,
        owner_id,
    ):

        stored_filename = self.storage.save_file(file)

        document = Document(
            filename=file.filename,
            stored_filename=stored_filename,
            content_type=file.content_type,
            owner_id=owner_id,
        )

        return self.repo.create(document)

    def list_documents(
        self,
        owner_id,
    ):

        return self.repo.get_all_for_user(owner_id)