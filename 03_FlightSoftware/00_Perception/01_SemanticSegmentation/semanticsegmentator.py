import cv2
import numpy as np

class SemanticSegmentator:
    def __init__(self, image, model_path, output_class_file, set_default_colors=True, color_file_path="colors.txt") -> None:
        # load input image and model
        self.image = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), (640, 480), interpolation=cv2.INTER_CUBIC)
        self.model = cv2.dnn.readNet(model_path)

        # load class .txt-file
        self.output_classes = open(output_class_file).read().strip().split("\n")

        # generate colors
        if set_default_colors:
            self.colors = open(color_file_path).read().strip().split("\n")
            self.colors = [np.array(c.split(",")).astype("int") for c in self.colors]
            self.colors = np.array(self.colors, dtype=np.uint8)
        else:
            np.random.seed(42)
            self.colors = np.random.randint(0, 255, size=(len(self.output_classes) - 1, 3), dtype=np.uint8)
            self.colors = np.vstack([[0, 0, 0], self.colors]).astype(np.uint8)

    def Segment(self):
        # create blob
        blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, (640, 480), 0, swapRB=True, crop=False)

        # execute model
        self.model.setInput(blob)
        output = self.model.forward()

        # get the segmentation map
        (n_classes, h, w) = output.shape[1:4]
        seg_map = np.argmax(output[0], axis=0)

        # construct mask and overlay
        mask = self.colors[seg_map]
        mask = cv2.resize(mask, (self.image.shape[1], self.image.shape[0]), interpolation=cv2.INTER_NEAREST)
        output = cv2.addWeighted(self.image, 0.3, mask, 0.7, 0)

        return output


