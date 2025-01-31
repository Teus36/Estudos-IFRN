import { View, Image, Text } from "react-native";
import tw from 'twrnc';


export default function Postagem({post}) {
    return (
        <View>
            <View>
                <Text>{post}</Text>
            </View>
            <View style={tw`flex flex-end flex-row gap-2`}>
                <Image style={tw`w-6 h-6`} source={require("./../assets/heart.png")}/>
                <Image style={tw`w-6 h-6`} source={require("./../assets/chat.png")}/>
                <Image style={tw`w-6 h-6`} source={require("./../assets/share.png")}/>
            </View>
        </View>
    )
}