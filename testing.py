from game_engine.speed_testing import SpeedTest

if __name__ == "__main__":
    SpeedTest().plot_differences(max_x=20, step=1, loop_times=10000, save_plot=True, filename="images/low_pixel_count.png")
    SpeedTest().plot_differences(max_x=70, step=5, loop_times=100, save_plot=True, filename="images/high_pixel_count.png")
