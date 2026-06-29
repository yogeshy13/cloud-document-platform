from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document):

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_all_for_user(
        self,
        owner_id,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.owner_id == owner_id
            )
            .all()
        )

    def get_by_id(
        self,
        document_id,
    ):

        return (
            self.db.query(Document)
            .filter(
                Document.id == document_id
            )
            .first()
        )

    def delete(
        self,
        document,
    ):

        self.db.delete(document)

        self.db.commit()