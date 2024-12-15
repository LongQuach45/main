from policy import Policy

def Policy2210xxx(Policy):
    def __init__(self, Policy):
        assert policy_id in [1, 2], "Policy ID must be 1 or 2"
        self.policy_id = policy_id
        # Student code here
        if policy_id == 1:
            pass
        elif policy_id == 2:
            pass

    def get_action(self, observation, info):
        # Student code here
        if self.policy_id == 1:
            return self.ffdh_policy(observation)
        elif self.policy_id == 2:
            return self.branch_policy(observation)
    def _get_ffdh_action(self, observation):
    # Sort products by height in descending order
        list_prods = sorted(
            observation["products"],
            key=lambda x: x["size"][0],  # Sort by height
            reverse=True
        )

    # Iterate over sorted products
        for prod in list_prods:
            if prod["quantity"] > 0:  # Only process if quantity > 0
                prod_size = prod["size"]
                prod_w, prod_h = prod_size

                # Iterate through available stocks
                for i, stock in enumerate(observation["stocks"]):
                    stock_w, stock_h = self._get_stock_size_(stock)

                    # Check if stock dimensions can accommodate the product
                    if stock_w >= prod_w and stock_h >= prod_h:
                    # Place the product at the first valid position
                        for y in range(stock_h - prod_h + 1):
                            for x in range(stock_w - prod_w + 1):
                                if self._can_place_(stock, (x, y), prod_size):
                                # Mark product as placed
                                    for row in range(y, y + prod_h):
                                        for col in range(x, x + prod_w):
                                            observation["stocks"][i][row][col] = 0

                                    prod["quantity"] -= 1  # Decrease quantity

                                    return {
                                        "stock_idx": i,
                                        "size": prod_size,
                                        "position": (x, y)
                                    }

    # Return default if no valid placement is found
        return {"stock_idx": -1, "size": [0, 0], "position": (0, 0)}
    def branch_policy(self, observation):
        # Sort products by height in descending order
        for prod in list_prods:
        # duyệt qua từng phần tử list_prods với index là prod
            if prod["quantity"] > 0:
                prod_size = prod["size"]
                #check if not out of stock then save it into prod_size array
                best_stock_idx = -1
                # best_position = None
                best_position = (None,None)
                min_waste = float('inf')

# Loop through all stocks
                for i, stock in enumerate(observation["stocks"]):
                #duyệt qua các phần tử observation["stocks"], lấy ra i và stock
                    stock_w, stock_h = self._get_stock_size_(stock)
                        #get height and weight of stock
                    prod_w, prod_h = prod_size
                        #get height and weight of product

                    if stock_w < prod_w or stock_h < prod_h:
                        continue
                        #check if available stock can hold product

                    # pos_x, pos_y = None, None
                    for x in range(stock_w - prod_w + 1):
        #loop with x là phần dư của prod khi đặt vào stock (chiều rộng)
                        for y in range(stock_h - prod_h + 1):
        #loop with y là phần dư của prod khi đặt vào stock (chiều dài)
                            if self._can_place_(stock, (x, y), prod_size):
                                # pos_x, pos_y = x, y
                                # Ưu tiên vị trí có ít ô trống nhất
                                waste_area = (stock[x:x+prod_w, y:y+prod_h] == -1).sum()
                                # Ưu tiên các vị trí gần góc trái dưới
                                distance_penalty = x + y

                                waste = 0.7 * waste_area + 0.3 * distance_penalty

                                # Cập nhật giải pháp tốt nhất
                                if waste < min_waste:
                                    min_waste = waste
                                    best_stock_idx = i
                                    best_position = (x, y)

                #Nếu tìm được vị trí
                if best_stock_idx != -1 and best_position is not None:
                    return {
                        "stock_idx": best_stock_idx,
                        "size":prod_size,
                        "position": best_position
                    }

        #Nếu không tìm được
        return {"stock_idx": -1, "size": [0, 0], "position": (0, 0)}
    # Student code here
# You can add more functions if needed
