import matplotlib.pyplot as plt
import numpy as np

# Basic plotting

# Open a new figure
plt.figure()

# plot X by Y
plt.plot(np.arange(1, 11), np.arange(1, 11) ** 2)
plt.show()

# Plot with log, it will overwrite previous if not on new 'plt.figure()'
plt.plot(np.arange(1, 11), np.log(np.arange(1, 11)))
plt.show()

# Overwriting with 'hold on' equivalent in Python ('plt.figure()' to ensure it doesn't overwrite previous plots)
plt.figure()
plt.plot(np.arange(1, 11), np.arange(1, 11) ** 2, linewidth=3)
# plot in red ('r'), with diamonds ('d') and thicker lines ('-')
plt.plot(np.arange(1, 11), np.log(np.arange(1, 11)) * 30, "r-d")
plt.show()

# Drawing a line with defined start and end points on the same graph without 'hold on'
plt.plot([2, 9], [60, 60], "k")
plt.plot([1, 10], [0, 100], "m")
plt.show()

# After 'hold off', plotting something else
plt.plot(np.arange(1, 11), np.arange(1, 11) * 3)
plt.show()

# Plotting information from variables
x = np.arange(0, 1.1, 0.1)
y = np.exp(x)
plt.plot(x, y, ".-")
plt.show()

# Plotting multiple lines simultaneously (in a matrix format)
plt.clf()  # clears the entire current figure with all its axes
plt.plot(np.arange(100, 1001, 100), np.random.rand(10, 3))
plt.title("Random lines")
plt.xlabel("x-axis label... maybe time? maybe space?")
plt.ylabel("voltage (\u03BCV)")  # Unicode for micro sign (µ)
plt.legend(["line 1", "line 2", "line 3"])
plt.show()

# Close a figure is automatic in pyplot when you start a new plot, but you can also explicitly close all figures
plt.close("all")

# plotting lines in 3D space
n = 10
dataX = np.random.rand(n)
dataY = np.random.randn(n)
dataZ = np.random.rand(n) * 10

plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(dataX, dataY, dataZ)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.zlabel("Z-axis")
plt.grid(True)
# enable 3D rotation of the plot
ax.grid(True)
plt.show()

# plotting with subplots
plt.figure()
for i, color in enumerate(["r", "g", "m", "k"]):
    plt.subplot(2, 2, i + 1)
    plt.plot(
        np.arange(1, i + 2),
        (np.arange(1, i + 2)) * 2 + 1,
        "m-p",
        linewidth=3,
        markeredgecolor=color,
    )
    plt.xlim([0.5, 4.5])
    plt.ylim([1, 10])
    plt.title(f'Subplot {i+1}!{"!" * i}')
plt.show()

# Basic image plotting
plt.figure()
plt.imshow(np.random.randn(100, 100), cmap="bone")
plt.colorbar()
plt.title('Plot using imshow with a "bone" colormap')
plt.show()

# Now for the individual subplots with different plotting functions and smoothing with a Gaussian
xyrange = np.arange(-1, 1.1, 0.1)
X, Y = np.meshgrid(xyrange, xyrange)
gaus2d = np.exp(-(X**2 + Y**2))

# View the Gaussian
plt.imshow(gaus2d)
plt.colorbar()
plt.show()

# When you want to save a figure, instead of using the GUI, you can save programmatically with:
# plt.savefig('figure.png') # for PNG format
# plt.savefig('figure.svg') # for SVG format
# plt.savefig('figure.eps') # for EPS format

# A bit more about images
# Images can be manipulated as Numpy arrays
amsterdam = plt.imread("amsterdam.bmp")
plt.imshow(amsterdam)
plt.axis("off")  # Hide axis
plt.title("Amsterdam Image")
plt.show()

# Try plotting the individual color channels
for i, color in enumerate(["Red channel", "Green channel", "Blue channel"]):
    plt.subplot(2, 2, i + 1)
    # Isolating color channels using indexing
    channel_data = amsterdam[:, :, i]
    plt.imshow(channel_data, cmap="gray")
    plt.title(color)
plt.subplot(2, 2, 4)
plt.imshow(amsterdam)
plt.title("All channels combined")
plt.show()
