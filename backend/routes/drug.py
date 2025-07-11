from fastapi import APIRouter

router = APIRouter(prefix="/drug")

drug_info = {
    "paracetamol": {
        "uses": "Pain relief, fever",
        "banned": False,
        "composition": "Paracetamol 500mg"
    },
    "thalidomide": {
        "uses": "Treatment for leprosy",
        "banned": True,
        "composition": "Thalidomide 100mg"
    },
}

@router.get("/search")
def search_drug(name: str):
    info = drug_info.get(name.lower())
    return info if info else {"error": "Drug not found"}
