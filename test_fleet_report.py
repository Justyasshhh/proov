def test_summary_handles_missing_last_service_km():
    fleet = [
        {"id": "VOS-7788", "odometer": 12000},  # missing last_service_km
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    ]
    summary = fleet_summary(fleet)
    assert summary["count"] == 2
    assert "average_wear" in summary
    assert summary["average_wear"] >= 0.0

