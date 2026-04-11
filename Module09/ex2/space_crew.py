
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import List, Self
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def requirements(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # 2. At least one Commander or Captain
        if not any(m.rank in [Rank.commander, Rank.captain] for m in
                   self.crew):
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")

        # 3. Long missions need 50% experienced crew (>=5 years)
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError("Long missions require at least "
                                 "50% experienced crew")

        # 4. All crew must be active
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        crew = [
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=35,
                specialization="Mission Command",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=30,
                specialization="Navigation",
                years_experience=6,
                is_active=True
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=4,
                is_active=True
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew,
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: {mission.budget_millions}M")
        print("Crew size:", len(crew))
        print("Crew members:")
        for creww in crew:
            print(f" - {creww.name} ({creww.rank.value}) - "
                  f"{creww.specialization}")

        print("\n=========================================")

        invalid_ranks = [
            CrewMember(
                member_id="C004",
                name="Mark Lee",
                rank=Rank.lieutenant,
                age=34,
                specialization="Navigation",
                years_experience=3),
            CrewMember(
                member_id="C005",
                name="Anna Bell",
                rank=Rank.officer,
                age=28,
                specialization="Science",
                years_experience=2)
            ]
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=invalid_ranks,
            mission_status="planned",
            budget_millions=2500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
