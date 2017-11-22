using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using UnityEngine.UI;
public class Provinces : MonoBehaviour
{
    /*This is the list of provinces, you can't access them as individually named objects anymore (for the sake of making the code modular) but you can
	search through the list and check, for example, if provinces.name == "Ireland" exists, and then return that Province object.*/
    public List<Province> provinces = new List<Province>();
    public List<int> provints = new List<int>();
    public static Provinces Instance;
    string placeholderstring;
    int placeholderint;

    void Awake()
    {
        Instance = this;
    }

    void Start()
    {
        loadJsonData();
    }

    void loadJsonData()
    {
        string filePath = Application.streamingAssetsPath + "/Provinces/";
        string[] files = System.IO.Directory.GetFiles(filePath);

        for (int i = 0; i < files.Length; i++)
        {
            if (files[i].EndsWith("json"))
            {
                Debug.Log("Grabbing " + files[i]);
                string dataAsJson = File.ReadAllText(files[i]); // Read the json from the filePath into a string.
                ProvinceFromJson provinceData = JsonUtility.FromJson<ProvinceFromJson>(dataAsJson); //Store that json into a provinceData struct.

                //Add a new Province object to the provinces List, giving it the JSON data grabbed from the aforementioned file.
                provinces.Add(new Province(provinceData.name, new float[] { provinceData.R, provinceData.G, provinceData.B }, provinceData.terrain_type, provinceData.prosperity, provinceData.owner));

                placeholderstring = provinceData.id;
                int.TryParse(placeholderstring, out placeholderint);
                provints.Add(placeholderint);
            }

        }
        /*foreach(Province str in provinces)
		{
			Debug.Log(str.name);
		}*/

    }
}

//Actual Province object that will be referenced and stored inside of a List<Province>.
public class Province
{
    public string sender;
    public float[] rgb = new float[3];
    public string terrainType;
    public float prosperity;
    public string owner;

    //Constructor, takes all the data that should be passed in from the provinceData object.
    public Province(string jsonName, float[] jsonRgb, string jsonTerrainType, float jsonProsperity, string jsonOwner)
    {
        sender = jsonName;
        for (int i = 0; i < rgb.Length; i++)
        {
            rgb[i] = jsonRgb[i];
        }
        terrainType = jsonTerrainType;
        prosperity = jsonProsperity;
        owner = jsonOwner;

    }
}

//Struct holding the data grabbed from the JSON file. This has to be the exact same layout as the content in the json file.
[System.Serializable]
public struct ProvinceFromJson
{
    
    public string sender;
    public float R;
    public float G;
    public float B;
    public string terrain_type;
    public string[] adjacencies;
    public float prosperity;
    public string owner;
}