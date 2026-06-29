from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File
from sqlalchemy.orm import Session
from uuid import UUID
from fastapi.responses import FileResponse
from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = DocumentService(db)

    return service.upload_document(
        file=file,
        owner_id=current_user.id,
    )


@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def list_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = DocumentService(db)

    return service.list_documents(
        current_user.id
    )

@router.get("/{document_id}/download")
def download_document(
    document_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = DocumentService(db)

    document = service.get_document(
        document_id,
        current_user.id,
    )

    path = service.storage.get_path(
        document.stored_filename
    )

    return FileResponse(
        path=path,
        filename=document.filename,
        media_type=document.content_type,
    )

@router.delete("/{document_id}")
def delete_document(
    document_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = DocumentService(db)

    service.delete_document(
        document_id,
        current_user.id,
    )

    return {
        "message": "Document deleted successfully"
    }