from flask import jsonify, request
from models.coupon import Coupon


def create_coupon_test():
    coupon_res = request.get_json()['coupon']
    discount_res = request.get_json()['discount']
    coupon = Coupon(code=coupon_res, discount_percentage=discount_res)
    coupon.save()
    return jsonify({'coupon': coupon.to_json()})

def get_coupons():
    couponObj = Coupon.objects()
    return jsonify({'coupons': [coupon.to_json() for coupon in couponObj]})


def check_coupon():
    coupon_res = request.get_json()['coupon']
    couponObj = Coupon.objects(code=coupon_res)
    if couponObj:
        return jsonify(couponObj[0].discount_percentage)
    else:
        return "Invalid Coupon"
