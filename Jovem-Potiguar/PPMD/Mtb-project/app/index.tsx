import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native'
import { useState } from 'react'
import tw from 'twrnc'

export default function Pagina1() {
    const [modalVisible, setModalVisible] = useState(false);
    return (
        <View>
            <Text style={style.text}>Hello World</Text>
            <TouchableOpacity onPress={() => setModalVisible(true)}>Abrir</TouchableOpacity>
            <Modal visible={modalVisible} animationType='slide'>
                <View style={}>
                    <Text>Modal aberto</Text>
                    <TouchableOpacity onPress={() => setModalVisible(false)}>Fechar</TouchableOpacity>
                </View>
            </Modal>
        </View>
    )
}

const style = StyleSheet.create({
    text: {
        color: 'red',
        fontSize: 25
    }
})