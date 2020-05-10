import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv ("C:\\Users\\User\\Desktop\\SENS\\2_putno\\Datos.csv")   
df = pd.DataFrame(data, columns= ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26','P27','P28','P29','P30','P31','P32','P33','P34','P35','P36','P37','P38','P39','P40','P41','P42','P43','P44','P45','P46','P47','P48','P49','P50','P51','P52','P53','P54','P55','P56','P57','P58','P59','P60','P61','P62','P63','P64','P65','P66','P67','P68','P69','P70','P71','P72','P73','P74','P75','P76','P77','P78','P79','P80','P81','P82','P83','P84','P85','P86','P87','P88','P89','P90','P91','P92','P93','P94','P95','P96','P97','P98','P99','P100','P101','P102','P103','P104','P105','P106','P107','P108','P109','P110','P111','P112','P113','P114','P115','P116','P117','P118','P119','Clases'])

# Connect to SQL Server
driverAzure = "ODBC Driver 17 for SQL Server"
serverAzure = "servidor-sens1.database.windows.net"
databaseAzure = "matrix"
usernameAzure = "admin_sens1"
passwordAzure = "ITM_s1jj"


conStringAzure = "DRIVER={{{}}};SERVER={};DATABASE={};UID={};PWD={}".format(driverAzure,serverAzure,databaseAzure,usernameAzure,passwordAzure)

conn = pyodbc.connect(conStringAzure)
cursor = conn.cursor()

# Create Table
cursor.execute('CREATE TABLE Proteins1 (P1    NVARCHAR(15),P2    NVARCHAR(15),P3    NVARCHAR(15),P4    NVARCHAR(15),P5    NVARCHAR(15),P6    NVARCHAR(15),P7    NVARCHAR(15),P8    NVARCHAR(15),P9    NVARCHAR(15),P10    NVARCHAR(15),P11    NVARCHAR(15),P12    NVARCHAR(15),P13    NVARCHAR(15),P14    NVARCHAR(15),P15    NVARCHAR(15),P16    NVARCHAR(15),P17    NVARCHAR(15),P18    NVARCHAR(15),P19    NVARCHAR(15),P20    NVARCHAR(15),P21    NVARCHAR(15),P22    NVARCHAR(15),P23    NVARCHAR(15),P24    NVARCHAR(15),P25    NVARCHAR(15),P26    NVARCHAR(15),P27    NVARCHAR(15),P28    NVARCHAR(15),P29    NVARCHAR(15),P30    NVARCHAR(15),P31    NVARCHAR(15),P32    NVARCHAR(15),P33    NVARCHAR(15),P34    NVARCHAR(15),P35    NVARCHAR(15),P36    NVARCHAR(15),P37    NVARCHAR(15),P38    NVARCHAR(15),P39    NVARCHAR(15),P40    NVARCHAR(15),P41    NVARCHAR(15),P42    NVARCHAR(15),P43    NVARCHAR(15),P44    NVARCHAR(15),P45    NVARCHAR(15),P46    NVARCHAR(15),P47    NVARCHAR(15),P48    NVARCHAR(15),P49    NVARCHAR(15),P50    NVARCHAR(15),P51    NVARCHAR(15),P52    NVARCHAR(15),P53    NVARCHAR(15),P54    NVARCHAR(15),P55    NVARCHAR(15),P56    NVARCHAR(15),P57    NVARCHAR(15),P58    NVARCHAR(15),P59    NVARCHAR(15),P60    NVARCHAR(15),P61    NVARCHAR(15),P62    NVARCHAR(15),P63    NVARCHAR(15),P64    NVARCHAR(15),P65    NVARCHAR(15),P66    NVARCHAR(15),P67    NVARCHAR(15),P68    NVARCHAR(15),P69    NVARCHAR(15),P70    NVARCHAR(15),P71    NVARCHAR(15),P72    NVARCHAR(15),P73    NVARCHAR(15),P74    NVARCHAR(15),P75    NVARCHAR(15),P76    NVARCHAR(15),P77    NVARCHAR(15),P78    NVARCHAR(15),P79    NVARCHAR(15),P80    NVARCHAR(15),P81    NVARCHAR(15),P82    NVARCHAR(15),P83    NVARCHAR(15),P84    NVARCHAR(15),P85    NVARCHAR(15),P86    NVARCHAR(15),P87    NVARCHAR(15),P88    NVARCHAR(15),P89    NVARCHAR(15),P90    NVARCHAR(15),P91    NVARCHAR(15),P92    NVARCHAR(15),P93    NVARCHAR(15),P94    NVARCHAR(15),P95    NVARCHAR(15),P96    NVARCHAR(15),P97    NVARCHAR(15),P98    NVARCHAR(15),P99    NVARCHAR(15),P100 NVARCHAR(15),P101 NVARCHAR(15),P102 NVARCHAR(15),P103 NVARCHAR(15),P104 NVARCHAR(15),P105 NVARCHAR(15),P106 NVARCHAR(15),P107 NVARCHAR(15),P108 NVARCHAR(15),P109 NVARCHAR(15),P110 NVARCHAR(15),P111 NVARCHAR(15),P112 NVARCHAR(15),P113 NVARCHAR(15),P114 NVARCHAR(15),P115 NVARCHAR(15),P116 NVARCHAR(15),P117 NVARCHAR(15),P118 NVARCHAR(15),P119 NVARCHAR(15),Clases NVARCHAR(4),)')
# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO matrix.dbo.Proteins1 (P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20,P21,P22,P23,P24,P25,P26,P27,P28,P29,P30,P31,P32,P33,P34,P35,P36,P37,P38,P39,P40,P41,P42,P43,P44,P45,P46,P47,P48,P49,P50,P51,P52,P53,P54,P55,P56,P57,P58,P59,P60,P61,P62,P63,P64,P65,P66,P67,P68,P69,P70,P71,P72,P73,P74,P75,P76,P77,P78,P79,P80,P81,P82,P83,P84,P85,P86,P87,P88,P89,P90,P91,P92,P93,P94,P95,P96,P97,P98,P99,P100,P101,P102,P103,P104,P105,P106,P107,P108,P109,P110,P111,P112,P113,P114,P115,P116,P117,P118,P119,Clases)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.P1,
                row.P2,
                row.P3,
                row.P4,
                row.P5,
                row.P6,
                row.P7,
                row.P8,
                row.P9,
                row.P10,
                row.P11,
                row.P12,
                row.P13,
                row.P14,
                row.P15,
                row.P16,
                row.P17,
                row.P18,
                row.P19,
                row.P20,
                row.P21,
                row.P22,
                row.P23,
                row.P24,
                row.P25,
                row.P26,
                row.P27,
                row.P28,
                row.P29,
                row.P30,
                row.P31,
                row.P32,
                row.P33,
                row.P34,
                row.P35,
                row.P36,
                row.P37,
                row.P38,
                row.P39,
                row.P40,
                row.P41,
                row.P42,
                row.P43,
                row.P44,
                row.P45,
                row.P46,
                row.P47,
                row.P48,
                row.P49,
                row.P50,
                row.P51,
                row.P52,
                row.P53,
                row.P54,
                row.P55,
                row.P56,
                row.P57,
                row.P58,
                row.P59,
                row.P60,
                row.P61,
                row.P62,
                row.P63,
                row.P64,
                row.P65,
                row.P66,
                row.P67,
                row.P68,
                row.P69,
                row.P70,
                row.P71,
                row.P72,
                row.P73,
                row.P74,
                row.P75,
                row.P76,
                row.P77,
                row.P78,
                row.P79,
                row.P80,
                row.P81,
                row.P82,
                row.P83,
                row.P84,
                row.P85,
                row.P86,
                row.P87,
                row.P88,
                row.P89,
                row.P90,
                row.P91,
                row.P92,
                row.P93,
                row.P94,
                row.P95,
                row.P96,
                row.P97,
                row.P98,
                row.P99,
                row.P100,
                row.P101,
                row.P102,
                row.P103,
                row.P104,
                row.P105,
                row.P106,
                row.P107,
                row.P108,
                row.P109,
                row.P110,
                row.P111,
                row.P112,
                row.P113,
                row.P114,
                row.P115,
                row.P116,
                row.P117,
                row.P118,
                row.P119,
                row.Clases,
                )
conn.commit()

