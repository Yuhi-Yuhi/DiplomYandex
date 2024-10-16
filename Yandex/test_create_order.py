import sender_stand_request

def test_create_order():
    track_order = sender_stand_request.create_order()
    get_order = sender_stand_request.get_order(track_order)
    assert get_order.status_code == 200
