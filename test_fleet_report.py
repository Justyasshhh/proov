def test_summary_handles_missing_last_service_km():
    # Car without last_service_km should not crash
    fleet = [
        {"id": "VOS-7788", "odometer": 12000},  # missing last_service_km
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    ]
    summary = fleet_summary(fleet)
    # It should still return a valid summary dict
    assert "count" in summary
    assert "due" in summary
    assert "average_wear" in summary
    # The missing car contributes 0 wear, so average is based only on valid cars
    assert summary["count"] == 2
    assert summary["average_wear"] >= 0.0
