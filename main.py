import pygame.display
from tensorflow import keras
import numpy as np
from utils import *


data_set = keras.datasets.mnist
(training_images, training_labels), (training_images2, training_labels2) = data_set.load_data()
combined_training_images = np.concatenate((training_images, training_images2))
combined_training_label = np.concatenate((training_labels, training_labels2))
training_images = combined_training_images/255.0

label_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

epochs = 5

neural_model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(118, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

neural_model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=['accuracy'])

training = neural_model.fit(training_images, combined_training_label, epochs=epochs)


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
run_loop = True
result = 'Draw First !'

def quit():
    global run_loop
    run_loop = False
    pygame.quit()

def grid_init(rows, collumns):
    grid = []
    for i in range(rows):
        grid.append([])
        for x in range(collumns):
            grid[i].append(background)
    return grid

def draw(window, grid, clear_button, text):
    window.fill(background)
    draw_grid(window, grid)
    draw_toolbar()
    clear_button.draw_button(window)
    test_button.draw_button(window)

    Button(200, height - toolbar_height/2 - 25, 50, 50, black, str(text), black).draw_result(window)
    pygame.display.update()

def draw_toolbar():
    pygame.draw.line(window, black, (0, height - toolbar_height), (width, height - toolbar_height), 1)
    pass

def draw_grid(window, grid):
    for i, row in enumerate(grid):
        for x, pixel in enumerate(row):
            pygame.draw.rect(window, pixel, (x * pixel_size, i * pixel_size, pixel_size, pixel_size))

def mouse_pos(position):
    x, y = position
    row = y // pixel_size
    column = x // pixel_size
    if row >= rows:
        raise IndexError
    return row, column


def test(test_grid):
    global grid
    global neural_model
    black_white_grid = []
    for i, row in enumerate(test_grid):
        black_white_grid.append([])
        for x in row:
            if x == black:
                black_white_grid[i].append(0.99215686)
            if x == white:
                black_white_grid[i].append(0.)
    self_test_image = np.array(black_white_grid)
    self_test_image = self_test_image.reshape(1, 28, 28)
    prediction = neural_model.predict(self_test_image)
    print('Prediction =', label_value[np.argmax(prediction)])
    return label_value[np.argmax(prediction)]




frame_clock = pygame.time.Clock()
grid = grid_init(rows, columns)
clear_button = Button(10, height - toolbar_height/2 - 25, 50, 50, black, 'Clear', black)
test_button = Button(70, height - toolbar_height/2 - 25, 50, 50, black, 'Test', black)


while run_loop:
    frame_clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            try:
                row, column = mouse_pos(position)
                grid[row][column] = black
            except IndexError:
                if clear_button.clicked(position):
                    result = 'Draw First !'
                    grid = grid_init(rows, columns)
                if test_button.clicked(position):
                    result = 'Prediction = %s'%(test(grid))

    draw(window, grid, clear_button, result)