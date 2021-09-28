# convert an image to text

# dependencies
import os, sys, cv2, numpy

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

class Parser:
    def __init__(self, MASK_RGB=False, img_path=False, testing=False):
        self.ss_path = ".data/images/ss.png" if not img_path else img_path

        self.testing = testing
        self.test_file_path = ".data/images/test_output/test_out.png"

        self.leggy_RGB = [255, 255, 88] if MASK_RGB == False else MASK_RGB

    def create_color_masked_image(self):
        """here bro:
        https://stackoverflow.com/questions/60704249/how-could-i-filter-an-image-by-using-a-single-rgb-color
        """
        original_img = cv2.imread(self.ss_path)
        t = 10

        cyan_thresh = cv2.inRange(original_img, numpy.array([self.leggy_RGB[2] - t, self.leggy_RGB[1] - t, self.leggy_RGB[0] - t]), numpy.array([self.leggy_RGB[2] + t, self.leggy_RGB[1] + t, self.leggy_RGB[0] + t]))

        mask_inv = 255 - cyan_thresh

        mask_rgb = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR)

        final_img = cv2.max(original_img, mask_rgb)

        if not self.testing:
            cv2.imwrite(self.ss_path, final_img)
        else:
            cv2.imwrite(self.test_file_path, final_img)

    def convert_img_to_BW(self):
        original_img = cv2.imread(self.ss_path)

        if self.testing:
            original_img = cv2.imread(self.test_file_path)

        # convert to gray scale
        gray_image = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

        # convert to black and white
        (thresh, black_and_white_image) = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY)

        # save the B&W image # TODO should this return instead??
        if not self.testing:
            cv2.imwrite(self.ss_path, black_and_white_image)
        else:
            cv2.imwrite(self.test_file_path, black_and_white_image)

    def parse_img(self):
        self.create_color_masked_image()

        self.convert_img_to_BW()


if __name__ == "__main__":
    read = Parser(img_path=".data/images/test/real_fake.png", testing=True)

    read.parse_img()
    