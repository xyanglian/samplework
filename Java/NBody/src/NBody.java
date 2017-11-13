import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import javax.swing.JFileChooser;

import princeton.StdAudio;
import princeton.StdDraw;

public class NBody {

	public static final double G = 6.67E-11;

	/**
	 * returns Euclidean distance between (x1, y1) and (x2, y2)
	 *
	 * @param x1
	 *            x-coordinate of point 1
	 * @param y1
	 *            y-coordinate of point 1
	 * @param x2
	 *            x-coordinate of point 2
	 * @param y2
	 *            y-coordinate of point 2
	 * @return Euclidean distance between (x1, y1) and (x2, y2)
	 */
	public double distance(double x1, double y1, double x2, double y2) {
		// calculates distance
		double distance = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
		return distance;

	}

	/**
	 * return the magnitude of the gravitational force between two bodies of
	 * mass m1 and m2 that are distance r apart
	 *
	 * @param m1
	 *            mass of body 1 in kg
	 * @param m2
	 *            mass of body 2 in kg
	 * @param r
	 *            distance in m
	 * @return force between m1 and m2 that are distance r apart
	 */
	public double force(double m1, double m2, double r) {
		// calculates force

		// prevents the situation in which the denominator is 0 when calculating
		// force

		if (r == 0) {
			return 0;

		}
		double f = G * m1 * m2 / (r * r);
		return f;

	}

	/**
	 * Returns the x positions and y positions of bodies
	 * 
	 * @param totalTime
	 *            The total amount of universe time to run for
	 * @param timeStep
	 *            The value of delta t in the equations to calculate position
	 * @param info
	 *            The scanner with info about the initial conditions of the
	 *            bodies
	 * @return an array whose first element is the x and y position of the first
	 *         body, and so on t = totalTime
	 */
	public double[][] positions(Scanner info, int totalTime, int timeStep) {

		int numPlanets = Integer.parseInt(info.next());

		double radius = Double.parseDouble(info.next());
		double[][] output = new double[numPlanets][2]; // Replace 0 with the
														// number of
		// bodies, read from the file
		// px[i], py[i], vx[i], vy[i], and mass[i] are the real numbers which
		// store the current position (x and y coordinates), velocity (x and y
		// components), and mass of planet i
		double[] px = new double[numPlanets];
		double[] py = new double[numPlanets];
		double[] vx = new double[numPlanets];
		double[] vy = new double[numPlanets];
		double[] mass = new double[numPlanets];
		// image[i] is a string that represents the filename of the image used
		// to display planet i.
		String[] image = new String[numPlanets];
		// fx[i] and fy[i] are arrays that store the net force acting on planet
		// i
		double[] fx = new double[numPlanets];
		double[] fy = new double[numPlanets];
		// ax and ay are accelerations in the x and y directions
		double ax[] = new double[numPlanets];
		double ay[] = new double[numPlanets];
		// creates a loop to plot the N bodies
		for (int i = 0; i < numPlanets; i++) {

			px[i] = Double.parseDouble(info.next());
			py[i] = Double.parseDouble(info.next());
			vx[i] = Double.parseDouble(info.next());
			vy[i] = Double.parseDouble(info.next());
			mass[i] = Double.parseDouble(info.next());
			image[i] = info.next();

		}
		info.close();
		// centers the picture and sets the boundaries of the simulation
		StdDraw.setXscale(-radius, radius);
		StdDraw.setYscale(-radius, radius);
		StdDraw.picture(0, 0, "data/starfield.jpg");
		// creates a loop to calculate the new velocity and position for each
		// body using timeStep for the duration of totalTime
		for (int l = 0; l < totalTime; l += timeStep) {
			for (int i = 0; i < numPlanets; i++) {
				fx[i] = 0;
				fy[i] = 0;
			}
			// clears the screen to re-center the picture and redraw the bodies
			// for the next timeStep
			StdDraw.clear();
			StdDraw.picture(0, 0, "data/starfield.jpg");
			// creates nested loops to calculate the net force acting on each
			// body
			for (int i = 0; i < numPlanets; i++) {
				for (int j = 0; j < numPlanets; j++) {
					// skips the case when i equals j
					if (i != j) {
						double d;
						d = distance(px[i], py[i], px[j], py[j]);
						double netforce;
						netforce = force(mass[i], mass[j], d);
						// stores the net force acting on planet i
						fx[i] += netforce * (px[j] - px[i]) / d;
						fy[i] += netforce * (py[j] - py[i]) / d;
					}

				}
			}
			// creates a loop to compute the acceleration instead of assuming it
			// is zero
			for (int i = 0; i < numPlanets; i++) {

				ax[i] = fx[i] / mass[i];

				ay[i] = fy[i] / mass[i];
				// updates velocity
				vx[i] += ax[i] * timeStep;
				vy[i] += ay[i] * timeStep;

			}
			//creates a loop to update position
			for (int i = 0; i < numPlanets; i++) {
				px[i] += timeStep * vx[i];
				py[i] += timeStep * vy[i];
				String img = image[i];
				StdDraw.picture(px[i], py[i], "data/" + img);
			}
			StdDraw.show(30);

		}
		//creates a loop to update output
		for (int i = 0; i < numPlanets; i++) {
			output[i][0] = px[i];
			output[i][1] = py[i];
		}
		return output;

	}

	public static void main(String[] args) {

		Scanner info = openFile();
		// inputs totalTime and timeStep
		int time = 10000000;
		int dt = 25000;

		if (info != null) {
			// plays the audio
			StdAudio.play("data/2001.mid");
			NBody myNBody = new NBody();
			double[][] results = myNBody.positions(info, time, dt);
			for (int i = 0; i < results.length; i++) {
				for (int j = 0; j < results[i].length; j++) {
					System.out.print(results[i][j] + " ");
				}
				System.out.println();
			}
			StdAudio.close();
		}
	}

	/**
	 * Displays file chooser for browsing in the project directory. and opens
	 * the selected file
	 *
	 * @return a new Scanner that produces values scanned from the selected
	 *         file. null if file could not be opened or was not selected
	 */

	public static Scanner openFile() {
		//Scanner reads the data file
		Scanner scan = null;
		System.out.println("Opening file dialog.");
		JFileChooser openChooser = new JFileChooser(System.getProperties().getProperty("user.dir"));

		int retval = openChooser.showOpenDialog(null);
		if (retval == JFileChooser.APPROVE_OPTION) {
			File file = openChooser.getSelectedFile();
			System.out.println(file.getAbsolutePath());
			try {
				scan = new Scanner(file);
				System.out.println("Opening: " + file.getName() + ".");
			} catch (FileNotFoundException e) {
				System.out.println("Could not open selected file.");
				e.printStackTrace();
			}
		} else {
			System.out.println("File open canceled.");
			System.exit(0);
		}

		return scan;
	}
}