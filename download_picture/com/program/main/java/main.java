import javax.net.ssl.*;

public class main{
    public static void main(String[] args) throws SSLException {
		try{
			//Get the bomb-1.gif
			String url = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/bomb-1.gif";
			String path="F:\\Cross-Fire\\bomb-1.git";
			Download download = new Download();
			download.downloadPicture(url,path);
			System.out.println("Sucessful download bomb-1.gif...");
			
			//Get the bomb-2.gif
			String url_2 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/bomb-2.gif";
			String path_2="F:\\Cross-Fire\\bomb-2.git";
			download.downloadPicture(url_2,path_2);
			System.out.println("Sucessful download bomb-2.gif...");
			
			//Get the bullet.png
			String url_3 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/bullet.png";
			String path_3="F:\\Cross-Fire\\bullet.png";
			download.downloadPicture(url_3,path_3);
			System.out.println("Sucessful download bullet.png...");
			
			//Get the cloud.png
			String url_4 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/cloud.png";
			String path_4 = "F:\\Cross-Fire\\cloud.png";
			download.downloadPicture(url_4,path_4);
			System.out.println("Sucessful download cloud.png...");
			
			//Get the dragon.png
			String url_5 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/dragon.png";
			String path_5 = "F:\\Cross-Fire\\dragon.png";
			download.downloadPicture(url_5,path_5);
			System.out.println("Sucessful download dragon.png...");
			
			//Get the flame.png
			String url_6 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/flame.png";
			String path_6 = "F:\\Cross-Fire\\flame.png";
			download.downloadPicture(url_6,path_6);
			System.out.println("Sucessful download flame.png...");
			
			//Get the gold.png
			String url_7 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/gold.png";
			String path_7 = "F:\\Cross-Fire\\gold.png";
			download.downloadPicture(url_7,path_7);
			System.out.println("Sucessful download gold.png...");
			
			//Get the missile.png
			String url_8 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/missile.png";
			String path_8 = "F:\\Cross-Fire\\missile.png";
			download.downloadPicture(url_8,path_8);
			System.out.println("Sucessful download missile.png...");
			
			//Get the plane.png
			String url_9 = "https://github.com/stepfencurryxiao/Cross-Fire/blob/master/image/plane.png";
			String path_9 = "F:\\Cross-Fire\\plane.png";
			download.downloadPicture(url_9,path_9);
			System.out.println("Sucessful download plane.png...");
			
			System.out.println("All the picture were downloaded!");
		}
		catch(Exception e){
			System.out.printf("Fail download!!!!");
		}
    }
}
