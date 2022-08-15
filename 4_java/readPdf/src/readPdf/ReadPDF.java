package readPdf;

import java.io.File;
import java.awt.Desktop;

public class ReadPDF {

	public static void main(String[] args) {

		try {

			File pdfFile = new File("C:\\Users\\crist\\Desktop\\ADS3003A.pdf");
			if (pdfFile.exists()) {

				if (Desktop.isDesktopSupported()) {
					Desktop.getDesktop().open(pdfFile);
				} else {
					System.out.println("Awt Desktop is not supported!");
				}

			} else {
				System.out.println("File is not exists!");
			}

			System.out.println("Done");

		} catch (Exception ex) {
			ex.printStackTrace();
		}

	}

}
