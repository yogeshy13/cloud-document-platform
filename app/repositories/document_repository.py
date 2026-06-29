from uuid import UUID
from sqlalchemy.orm import Session
from app.models.document import Document
from uuid import UUID
from fastapi import HTTPException


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document):
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_all_for_user(self, owner_id: UUID):
        return (
            self.db.query(Document)
            .filter(Document.owner_id == owner_id)
            .all()
        )

    def get_by_id(self, document_id: UUID):
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def delete(self, document: Document):
        self.db.delete(document)
        self.db.commit()

    def file_exists(self, stored_filename: str):

         return (
                    self.upload_dir / stored_filename
                ).exists()


    def get_path(self, stored_filename: str):

            return (
                self.upload_dir / stored_filename
            )
    
    def get_document(
            self,
            document_id: UUID,
            owner_id: UUID,
        ):
        document = self.repo.get_by_id(document_id)

        if document is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found"
                )

        if document.owner_id != owner_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
                )

        return document
    

    def delete_document(
        self,
        document_id: UUID,
        owner_id: UUID,
    ):
        document = self.get_document(
        document_id,
        owner_id,
    )

        self.storage.delete_file(
            document.stored_filename
        )

        self.repo.delete(document)