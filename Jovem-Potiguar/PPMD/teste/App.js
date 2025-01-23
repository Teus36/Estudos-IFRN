import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { TextInput } from 'react-native-web';
import { Button, Image } from 'react-native'

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/favicon.png')} />
      <Text>Hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</Text>
      <TextInput placeholder='Digite algo...' style={styles.input}></TextInput>
      <View style={styles.buttonContainer}>
        <Button title="Cadastrar" onPress={() => alert('Botão clicado!')} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    width: '40%',
    padding: '7px',
    backgroundColor: '#e4e1e1',
    borderRadius: '10px',
  },
  buttonContainer: {
    marginTop: '10px',
  }
});


