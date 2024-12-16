from policy import Policy
import pulp

class Policy2210xxx(Policy):
    def __init__(self, policy_id=1):
        super().__init__()
        assert policy_id in [1, 2], "Policy ID must be 1 or 2"

        # Student code here
        self.policy_id = policy_id 

    def get_action(self, observation, info):
        # Student code here
        if self.policy_id == 1:  # Best Fit Policy
            return self.best_fit_policy(observation, info)
        elif self.policy_id == 2:   #Dynamic Programming Policy
            return self.dynamic_programming_policy(observation, info)


    # Student code here
    def best_fit_policy(self, observation, info):
        list_prods = observation["products"]
        best_fit = None
        min_waste = float("inf") 

        for prod in list_prods:
            if prod["quantity"] > 0:  # Chỉ xét sản phẩm có số lượng > 0
                prod_size = prod["size"]

                for stock_idx, stock in enumerate(observation["stocks"]):
                    stock_w, stock_h = self._get_stock_size_(stock)
                    prod_w, prod_h = prod_size

                    # Kiểm tra cả 2 cách đặt (không xoay và xoay sản phẩm)
                    for rotated in [False, True]:
                        if rotated:
                            prod_w, prod_h = prod_h, prod_w

                        if stock_w >= prod_w and stock_h >= prod_h:
                            for x in range(stock_w - prod_w + 1):
                                for y in range(stock_h - prod_h + 1):
                                    if self._can_place_(stock, (x, y), (prod_w, prod_h)):
                                        # Tính diện tích thừa
                                        waste = (stock_w * stock_h) - (prod_w * prod_h)
                                        if waste < min_waste:
                                            min_waste = waste
                                            best_fit = {
                                                "stock_idx": stock_idx,
                                                "size": (prod_w, prod_h),
                                                "position": (x, y),
                                            }
        return best_fit
    def dynamic_programming_policy(self, observation, info):
        list_prods = observation["products"]
        stocks = observation["stocks"]

        best_fit = None  # Hành động tối ưu
        min_trim_loss = float("inf")  # Lượng lãng phí tối thiểu

        for stock_idx, stock in enumerate(stocks):
            stock_w, stock_h = self._get_stock_size_(stock)

            # Tạo bảng DP để lưu lượng cắt tối ưu cho mỗi kích thước
            dp = [[0] * (stock_h + 1) for _ in range(stock_w + 1)]
            cut_positions = [[None] * (stock_h + 1) for _ in range(stock_w + 1)]

            # Duyệt qua các sản phẩm
            for prod in list_prods:
                if prod["quantity"] > 0:  # Chỉ xét sản phẩm còn số lượng
                    prod_w, prod_h = prod["size"]

                    # Duyệt qua bảng DP để tìm cách đặt sản phẩm
                    for w in range(stock_w, prod_w - 1, -1):
                        for h in range(stock_h, prod_h - 1, -1):
                            # Nếu đặt được sản phẩm tại kích thước này
                            if dp[w - prod_w][h - prod_h] + prod_w * prod_h > dp[w][h]:
                                dp[w][h] = dp[w - prod_w][h - prod_h] + prod_w * prod_h
                                cut_positions[w][h] = (prod_w, prod_h)

            # Tìm kích thước tối ưu trong bảng DP
            for w in range(stock_w + 1):
                for h in range(stock_h + 1):
                    trim_loss = (stock_w * stock_h) - dp[w][h]  # Lượng vật liệu thừa
                    if trim_loss < min_trim_loss:
                        min_trim_loss = trim_loss
                        if cut_positions[w][h]:
                            prod_w, prod_h = cut_positions[w][h]
                            best_fit = {
                                "stock_idx": stock_idx,
                                "size": (prod_w, prod_h),
                                "position": (stock_w - w, stock_h - h),
                            }

        return best_fit if best_fit else {"stock_idx": -1, "size": [0, 0], "position": (0, 0)}


    # You can add more functions if needed
