    available_moves = set((i, j) for i in range(self.height) for j in range(self.width))
        unchosen_moves = available_moves - self.moves_made
        safe_moves = unchosen_moves - self.mines

        if safe_moves:
            return random.choice(list(safe_moves))
        elif unchosen_moves:
            return random.choice(list(unchosen_moves))
        else:
            return None