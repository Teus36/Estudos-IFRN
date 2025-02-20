import { View, Text, StyleSheet, TouchableOpacity, Modal, Switch } from 'react-native'
import { SafeAreaView, SafeAreaProvider } from 'react-native-safe-area-context'
import { useState } from 'react'
import tw from 'twrnc'

export default function Pagina1() {
    const [modalVisible, setModalVisible] = useState(false)
    const [isEnabled, setIsEnabled] = useState(false) // Estado do switch
    const [count, setCount] = useState(0)

    const increase = () => {
        setCount(count + 1)
    }

    const decrease = () => {
        setCount(count - 1)
    }
    return (
        <SafeAreaProvider>
            <SafeAreaView style={tw`flex-1 justify-center items-center`}>
                <View style={tw`mx-auto`}>
                    <Text style={style.text}>Hello World</Text>

                    {/* Botão para abrir o modal */}
                    <TouchableOpacity onPress={() => setModalVisible(true)} style={tw`my-4`}>
                        <Text style={tw`text-blue-500`}>Abrir Modal</Text>
                    </TouchableOpacity>

                    {/* Modal */}
                    <Modal visible={modalVisible} animationType='slide'>
                        <View style={tw`flex-1 justify-center items-center gap-10`}>
                            <TouchableOpacity
                                onPress={() => setModalVisible(false)}
                                style={tw`bg-red-400 w-32 h-16 justify-center items-center rounded-2xl`}>
                                <Text style={tw`text-white`}>Fechar</Text>
                            </TouchableOpacity>
                        </View>
                    </Modal>

                    {/* Switch (Toggle) */}
                    <View style={tw`my-4 items-center`}>
                        <Text>{isEnabled ? 'Ativado' : 'Desativado'}</Text>
                        <Switch
                            value={isEnabled}
                            onValueChange={setIsEnabled} // Alterna o estado
                            trackColor={{ false: "#767577", true: "#81b0ff" }}
                            thumbColor={isEnabled ? "#595ff9" : "#FFFFFF"}
                        />
                    </View>
                    <View style={tw`mx-auto`}>
                    <Text style={style.text}>Contador: {count}</Text>

                    {/* Botões para aumentar e diminuir */}
                    <View style={tw`flex-row gap-4`}>
                        <TouchableOpacity onPress={increase} style={tw`bg-blue-500 p-4 rounded-full`}>
                            <Text style={tw`text-white`}>Aumentar</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={decrease} style={tw`bg-red-500 p-4 rounded-full`}>
                            <Text style={tw`text-white`}>Diminuir</Text>
                        </TouchableOpacity>
                    </View>
                </View>
                </View>
            </SafeAreaView>
        </SafeAreaProvider>
    )
}

const style = StyleSheet.create({
    text: {
        color: 'red',
        fontSize: 25
    }
})
