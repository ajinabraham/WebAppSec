import java.io.FileInputStream;
import java.io.FileNotFoundException;
import org.opensaml.xml.parse.BasicParserPool;
import org.w3c.dom.Document;

public class Vuln {

	public static void main(String args[]) throws Exception, FileNotFoundException
	{
		//XML Parser XXE test
	
	    BasicParserPool parser = new BasicParserPool();
		FileInputStream fis = new FileInputStream("/Users/xxx/Desktop/xml.xml");
    	Document doc = parser.parse(fis);
        System.out.println(doc.getDocumentElement());
        
		}
}

