import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração de visualização
pd.set_option('display.max_columns', 42)

# Carregar o dataset
building_energy = pd.read_csv('2015-building-energy-benchmarking.csv')
print(building_energy.head())
print(building_energy.dtypes)

# Verificar e preencher valores faltantes
faltantes = building_energy.isnull().sum()
faltantes_percentual = (faltantes / len(building_energy)) * 100
print(faltantes_percentual)

# Preenchendo a coluna 'ENERGYSTARScore' com a mediana
building_energy['ENERGYSTARScore'] = building_energy['ENERGYSTARScore'].fillna(
    building_energy['ENERGYSTARScore'].median()
)

# Atualizar valores faltantes após preenchimento
faltantes = building_energy.isnull().sum()
faltantes_percentual = (faltantes / len(building_energy)) * 100
print(faltantes_percentual)

# Selecionar colunas numéricas para correlação
colunas_numericas = [
    'NumberofBuildings', 'NumberofFloors', 'PropertyGFATotal',
    'PropertyGFAParking', 'PropertyGFABuilding(s)', 'LargestPropertyUseTypeGFA',
    'SecondLargestPropertyUseTypeGFA', 'ThirdLargestPropertyUseTypeGFA',
    'ENERGYSTARScore', 'SiteEUI(kBtu/sf)', 'SiteEUIWN(kBtu/sf)',
    'SourceEUI(kBtu/sf)', 'SourceEUIWN(kBtu/sf)', 'SiteEnergyUse(kBtu)',
    'SiteEnergyUseWN(kBtu)', 'SteamUse(kBtu)', 'Electricity(kWh)',
    'Electricity(kBtu)', 'NaturalGas(therms)', 'NaturalGas(kBtu)',
    'OtherFuelUse(kBtu)', 'GHGEmissions(MetricTonsCO2e)',
    'GHGEmissionsIntensity(kgCO2e/ft2)'
]

dados = building_energy[colunas_numericas].apply(pd.to_numeric, errors='coerce')

# Criar o heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(dados.corr())
plt.title('Heatmap de Correlação')
plt.show()
