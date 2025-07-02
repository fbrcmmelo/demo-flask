class PaginationInput:
    def __init__(self, page: int = 1, limit: int = 10):
        self.page = page
        self.limit = limit

    def to_dict(self):
        return {
            "page": self.page,
            "limit": self.limit
        }
