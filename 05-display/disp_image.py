from PIL import Image
import time
import serial

image = Image.open(r"C:\Users\maxaz\Desktop\f.jpg").convert("RGB")

# под размер экрана после rotation 90
image = image.resize((320, 240))

width, height = image.size

def main():
    ser = serial.Serial('COM15', 115200, timeout=1)
    time.sleep(2)

    print(f"Port {ser.name} opened")

    try:
        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))

                color888 = (r << 16) | (g << 8) | b

                ser.write(f"disp_px {x} {y} 0x{color888:06X}\n".encode("ascii"))

    finally:
        ser.close()
        print("Port closed")

if __name__ == "__main__":
    main()