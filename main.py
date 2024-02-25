"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def subquadratic_multiply(x, y):

  # derived from lab 3 quadratic multiply work:

  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)

  xdec = x.decimal_val
  ydec = y.decimal_val

  if (xdec <= 1) and (ydec <= 1):
    return BinaryNumber(xdec * ydec)

  else:
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    # implementing formula in small steps to eventually combine:

    left_product = (subquadratic_multiply(x_left, y_left))
    right_product = (subquadratic_multiply(x_right, y_right))

    x_left_dec = x_left.decimal_val
    y_left_dec = y_left.decimal_val
    x_right_dec = x_right.decimal_val
    y_right_dec = y_right.decimal_val

    leftprod_dec = left_product.decimal_val
    rightprod_dec = right_product.decimal_val

    x_sum = BinaryNumber(x_left_dec + x_right_dec)
    y_sum = BinaryNumber(y_left_dec + y_right_dec)

    middle = BinaryNumber(
        subquadratic_multiply(x_sum, y_sum).decimal_val - leftprod_dec -
        rightprod_dec)

    product_left = bit_shift(left_product, len(xvec))
    product_middle = bit_shift(middle, len(xvec) // 2)

    prodleft_dec = product_left.decimal_val
    prodmid_dec = product_middle.decimal_val

    return (prodleft_dec + prodmid_dec + rightprod_dec)


def time_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  return (time.time() - start) * 1000
