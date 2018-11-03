from game_engine.speed_testing import SpeedTest

if __name__ == "__main__":
    SpeedTest().plot_differences(max_x=50, step=10, loop_times=15)
