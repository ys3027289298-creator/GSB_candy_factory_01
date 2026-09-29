import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_feed(self):
        state = core.new_game()
        self.assertTrue(core.feed(state, 1, 10))
        self.assertFalse(core.feed(state, 1, 10))

    def test_02_pot_capacity(self):
        state = core.new_game()
        state["pot_load"] = 2
        result = core.boil(state, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases_pot(self):
        state = core.new_game()
        core.boil(state, 1)
        core.cancel(state, 1)
        self.assertEqual(state["pot_load"], 0)

    def test_05_no_pour_without_syrup(self):
        state = core.new_game()
        state["syrup"] = 0
        result = core.pour(state, 10)
        self.assertFalse(result)

    def test_06_crack_once(self):
        state = core.new_game()
        core.crack(state)
        self.assertEqual(state["rate"], 90)

    def test_07_no_cool_without_cooling(self):
        state = core.new_game()
        state["cooling"] = 0
        result = core.cool(state, 1)
        self.assertFalse(result)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
