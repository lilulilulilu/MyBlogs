#!/usr/bin/env python3
"""
查询 Weaviate 中的所有数据
展示如何获取和查看 Weaviate 中存储的所有数据
"""

import weaviate
import json
from langchain_community.vectorstores import Weaviate
from langchain.docstore.document import Document
from langchain_dashscope import DashScopeEmbeddings


    
# 1. 初始化客户端
client = weaviate.Client("http://localhost:8080")
    

def export_all_data(client):
    """导出所有数据"""
    print("\n5. 导出所有数据：")
    
    try:
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        all_data = {}
        
        for class_info in classes:
            class_name = class_info["class"]
            print(f"   导出类: {class_name}")
            
            try:
                # 获取所有对象 - 包含完整的_additional信息和所有属性
                # 首先获取类的属性列表
                properties = [prop["name"] for prop in class_info.get("properties", [])]
                result = client.query.get(class_name, properties).with_additional(["id", "vector", "creationTimeUnix", "lastUpdateTimeUnix", "distance"]).do()
                objects = result.get("data", {}).get("Get", {}).get(class_name, [])
                
                all_data[class_name] = objects
                print(f"   ✅ 导出 {len(objects)} 个对象")
                
            except Exception as e:
                print(f"   ❌ 导出类 {class_name} 失败: {e}")
                all_data[class_name] = []
        
        # 保存到文件
        output_file = "weaviate_all_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n   ✅ 所有数据已导出到: {output_file}")
        
        # 显示统计信息
        total_objects = sum(len(objects) for objects in all_data.values())
        print(f"   📊 统计信息:")
        print(f"     总类数: {len(classes)}")
        print(f"     总对象数: {total_objects}")
        
        for class_name, objects in all_data.items():
            print(f"     {class_name}: {len(objects)} 个对象")
        
    except Exception as e:
        print(f"   ❌ 导出数据失败: {e}")

def query_with_filters(client):
    """使用过滤器查询数据"""
    print("\n6. 使用过滤器查询数据：")
    
    try:
        schema = client.schema.get()
        classes = schema.get("classes", [])
        
        for class_info in classes:
            class_name = class_info["class"]
            properties = class_info.get("properties", [])
            
            print(f"\n   查询类: {class_name}")
            
            # 查找可能的过滤字段
            filterable_properties = []
            for prop in properties:
                prop_name = prop.get("name", "")
                prop_type = prop.get("dataType", [])
                if prop_name and prop_type:
                    filterable_properties.append((prop_name, prop_type))
            
            if not filterable_properties:
                print("   ⚠️  没有可过滤的属性")
                continue
            
            print(f"   可过滤的属性: {[p[0] for p in filterable_properties[:3]]}")
            
            # 尝试一些常见的过滤查询
            try:
                # 查询前10个对象
                properties = [prop["name"] for prop in class_info.get("properties", [])]
                result = client.query.get(class_name, properties).with_additional(["id", "vector", "creationTimeUnix", "lastUpdateTimeUnix", "distance"]).with_limit(10).do()
                objects = result.get("data", {}).get("Get", {}).get(class_name, [])
                
                if objects:
                    print(f"   ✅ 找到 {len(objects)} 个对象（前10个）")
                    
                    # 显示第一个对象的属性作为示例
                    first_obj = objects[0]
                    print("   示例对象属性:")
                    for key, value in first_obj.items():
                        if key != "_additional":
                            if isinstance(value, str) and len(value) > 50:
                                value = value[:50] + "..."
                            print(f"     {key}: {value}")
                else:
                    print("   ⚠️  该类中没有数据")
                    
            except Exception as e:
                print(f"   ❌ 查询失败: {e}")
                
    except Exception as e:
        print(f"   ❌ 过滤查询失败: {e}")

if __name__ == "__main__":
    # 执行所有查询方法
    export_all_data(client)

