import java.awt.Color;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import javax.imageio.ImageIO;

public class MakeStego {

    public static void main( final String[] args ) {
        String path = "/home/c/Desktop/NCL/Stego_3.txt";
        ArrayList<String[]> lines = new ArrayList<>();
        try{
            String line = "";
            FileReader input = new FileReader(path);
            BufferedReader br = new BufferedReader(input);

            while ((line = br.readLine()) != null){
                String[] temp = line.split(" ");
                temp[0] = temp[0].substring(0, temp[0].length()-1);
                lines.add(temp);
            }
            br.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }

        String[] lastLine = lines.get(lines.size()-1);
        String height = lastLine[0].substring(0, lastLine[0].indexOf(","));
        String width = lastLine[0].substring(lastLine[0].indexOf(",")+1);

        BufferedImage img = map(Integer.parseInt(height), Integer.parseInt(width), lines);
        savePNG( img, "/home/c/Desktop/NCL/Stego_out.png" );
    }

private static BufferedImage map( int sizeX, int sizeY, ArrayList<String[]> data){
        final BufferedImage res = new BufferedImage( sizeY, sizeX, BufferedImage.TYPE_INT_RGB );
        int count = 0;
        for (int x = 0; x < sizeX; x++){
            for (int y = 0; y < sizeY; y++){
                String[] temp = data.get(count);
                count++;
                Color tempColor = Color.decode(temp[2]);
                if (tempColor.getRGB() == Color.WHITE.getRGB()){
                    tempColor = new Color(Color.PINK.getRGB());
                }
                res.setRGB(y, x, tempColor.getRGB());
            }
        }
        return res;
    }

    private static void savePNG( final BufferedImage bi, final String path ){
        try {
            RenderedImage rendImage = bi;
            // ImageIO.write(rendImage, "bmp", new File(path));
            ImageIO.write(rendImage, "PNG", new File(path));
            // ImageIO.write(rendImage, "jpeg", new File(path));
        } catch ( IOException e) {
            e.printStackTrace();
        }
    }

}
