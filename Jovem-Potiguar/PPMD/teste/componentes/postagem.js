import { View, Image, Text, TouchableOpacity } from "react-native";
import tw from 'twrnc';
import { useState } from 'react'


export default function Postagem({post}) {
    const [like, setLike] = useState(false)

    return (
        <View style={tw`p-5 border-2 border-black rounded-lg`}>
            <View>
                <Text>{post}</Text>
            </View>
            <View style={tw`flex flex-end flex-row gap-2 mt-5`}>
                <TouchableOpacity onPress={(e) => setLike(!like)}>
                    {like 
                    ? <Image style={tw`w-6 h-6`} source={require("./../assets/heart_fill.png")}/>
                    : <Image style={tw`w-6 h-6`} source={require("./../assets/heart.png")}/>
                    }
                </TouchableOpacity>
                <Image style={tw`w-6 h-6`} source={require("./../assets/chat.png")}/>
                <Image style={tw`w-6 h-6`} source={require("./../assets/share.png")}/>
            </View>
        </View>
    )
}