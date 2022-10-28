from flask import Blueprint

from controller.booking_room_controller import book_room_controller, get_booking_rooms_controller, \
    get_booking_room_controller

booking_route = Blueprint('booking_route', __name__)


@booking_route.route('/booking/room', methods=['POST'])
def book_room():
    return book_room_controller()


@booking_route.route('/booking/room', methods=['GET'])
def get_rooms():
    return get_booking_rooms_controller()


@booking_route.route('/booking/room/availability', methods=['POST'])
def get_rooms_availability():
    return get_booking_room_controller()
