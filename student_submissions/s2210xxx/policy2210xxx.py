from policy import Policy

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Policy2210xxx(Policy):
    def __init__(self, policy_id=1):
        assert policy_id in [1, 2], "Policy ID must be 1 or 2"

        # Student code here
        if policy_id == 1:
            pass
        elif policy_id == 2:
            pass

    def get_action(self, observation, info):
        prod_size = [0, 0]
        stock_idx = -1
        pos_x, pos_y = 0, 0

        list_prods = observation["products"]

        rectangles = [Rectangle(prod["size"][0], prod["size"][1]) for prod in list_prods if prod["quantity"] > 0]
        # Sắp xếp các hình chữ nhật theo diện tích giảm dần
        rectangles.sort(key=lambda x: x.width * x.height, reverse=True)

        # Pick a product that has quality > 0
        for rectangle in rectangles:
            prod_size = (rectangle.width, rectangle.height)
            # Loop through all stocks
            for i, stock in enumerate(observation["stocks"]):
                stock_w, stock_h = self._get_stock_size_(stock)
                prod_w, prod_h = prod_size
                if stock_w >= prod_w and stock_h >= prod_h:
                    pos_x, pos_y = None, None
                    for x in range(stock_w - prod_w + 1):
                        for y in range(stock_h - prod_h + 1):
                            if self._can_place_(stock, (x, y), prod_size):
                                pos_x, pos_y = x, y
                                break
                        if pos_x is not None and pos_y is not None:
                            break
                    if pos_x is not None and pos_y is not None:
                        stock_idx = i
                        break

                if stock_w >= prod_h and stock_h >= prod_w:
                    pos_x, pos_y = None, None
                    for x in range(stock_w - prod_h + 1):
                        for y in range(stock_h - prod_w + 1):
                            if self._can_place_(stock, (x, y), prod_size[::-1]):
                                prod_size = prod_size[::-1]
                                pos_x, pos_y = x, y
                                break
                        if pos_x is not None and pos_y is not None:
                            break
                    if pos_x is not None and pos_y is not None:
                        stock_idx = i
                        break

            if pos_x is not None and pos_y is not None:
                break

        return {"stock_idx": stock_idx, "size": prod_size, "position": (pos_x, pos_y)}

    # Student code here
    # You can add more functions if needed
