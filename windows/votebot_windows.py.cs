
using Firefox = selenium.webdriver.Firefox;

using Options = selenium.webdriver.firefox.options.Options;

using webdriver = selenium.webdriver;

using WebDriverWait = selenium.webdriver.support.ui.WebDriverWait;

using EC = selenium.webdriver.support.expected_conditions;

using TimeoutException = selenium.common.exceptions.TimeoutException;

using By = selenium.webdriver.common.by.By;

using yaml;

using time;

using os;

using System.Diagnostics;

public static class votebot_windows {
    
    public static object data = yaml.load(f, Loader: yaml.FullLoader);
    
    public static object username_file = data["username_file"];
    
    public static object server = data["server"];
    
    public static object headless = data["headless"];
    
    public static string CURR_DIR = os.path.dirname(os.path.realpath(@__file__));
    
    public static object opts = Options();
    
    public static void vote(object User) {
        Console.WriteLine("Operating in Windows Mode");
        var path = CURR_DIR + "\geckodriver.exe";
        var browser = Firefox(executable_path: path, options: opts);
        var addon = CURR_DIR + "\\uBlock0@raymondhill.net.xpi";
        browser.install_addon(addon);
        Console.WriteLine("Inserting uBlock");
        Console.WriteLine("Voting for " + User + "!");
        browser.get(server);
        time.sleep(5);
        if (browser.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[2]")) {
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[2]").click();
            Console.WriteLine("Accepted Cookies");
        }
        browser.execute_script("document.body.style.MozTransform = \"scale(0.5)\";");
        Console.WriteLine("Scaling to 0.5");
        time.sleep(10);
        var I = browser.find_element_by_xpath("//*[@id=\"playername\"]");
        Console.WriteLine("Scrolling into View");
        browser.execute_script("arguments[0].scrollIntoView(true);", I);
        time.sleep(10);
        var player = browser.find_element_by_xpath("//*[@id=\"playername\"]");
        player.send_keys(User);
        Console.WriteLine("Inserting Username");
        I = browser.find_element_by_xpath("//*[@id=\"captcha\"]");
        Console.WriteLine("Scrolling into View");
        browser.execute_script("arguments[0].scrollIntoView(true);", I);
        time.sleep(10);
        browser.find_element_by_xpath("//*[@id=\"captcha\"]").click();
        Console.WriteLine("Voting");
        time.sleep(10);
        var c = browser.current_url;
        //'fail' in c
        if (c.find("fail") != -1) {
            Console.WriteLine("Already Voted/Failed to vote");
        } else {
            Console.WriteLine("Sucessfully voted");
        }
        time.sleep(5);
        browser.close();
    }
    
    static votebot_windows() {
        opts.set_headless();
        vote(line.strip());
    }
    
    static votebot_windows() {
        using (var f = open("config.yaml")) {
        }
        Console.WriteLine(CURR_DIR);
        if (headless == "1") {
            Debug.Assert(opts.headless);
        }
        using (var textFile = open(username_file)) {
            foreach (var line in textFile) {
            }
        }
    }
}
