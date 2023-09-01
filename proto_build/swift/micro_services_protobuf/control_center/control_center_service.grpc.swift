//
// DO NOT EDIT.
// swift-format-ignore-file
//
// Generated by the protocol buffer compiler.
// Source: micro_services_protobuf/control_center/control_center_service.proto
//
import GRPC
import NIO
import NIOConcurrencyHelpers
import SwiftProtobuf


/// Usage: instantiate `ControlCenter_ImportantInfoServiceClient`, then call methods of this protocol to make API calls.
public protocol ControlCenter_ImportantInfoServiceClientProtocol: GRPCClient {
  var serviceName: String { get }
  var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? { get }

  func forceRefreshHomepageInfoCache(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions?
  ) -> UnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>

  func getHomepageInfos(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions?
  ) -> UnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>
}

extension ControlCenter_ImportantInfoServiceClientProtocol {
  public var serviceName: String {
    return "control_center.ImportantInfoService"
  }

  /// 强制刷新首页信息缓存
  ///
  /// - Parameters:
  ///   - request: Request to send to ForceRefreshHomepageInfoCache.
  ///   - callOptions: Call options.
  /// - Returns: A `UnaryCall` with futures for the metadata, status and response.
  public func forceRefreshHomepageInfoCache(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) -> UnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse> {
    return self.makeUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.forceRefreshHomepageInfoCache.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeForceRefreshHomepageInfoCacheInterceptors() ?? []
    )
  }

  /// 获取首页信息
  ///
  /// - Parameters:
  ///   - request: Request to send to GetHomepageInfos.
  ///   - callOptions: Call options.
  /// - Returns: A `UnaryCall` with futures for the metadata, status and response.
  public func getHomepageInfos(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) -> UnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse> {
    return self.makeUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.getHomepageInfos.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeGetHomepageInfosInterceptors() ?? []
    )
  }
}

@available(*, deprecated)
extension ControlCenter_ImportantInfoServiceClient: @unchecked Sendable {}

@available(*, deprecated, renamed: "ControlCenter_ImportantInfoServiceNIOClient")
public final class ControlCenter_ImportantInfoServiceClient: ControlCenter_ImportantInfoServiceClientProtocol {
  private let lock = Lock()
  private var _defaultCallOptions: CallOptions
  private var _interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol?
  public let channel: GRPCChannel
  public var defaultCallOptions: CallOptions {
    get { self.lock.withLock { return self._defaultCallOptions } }
    set { self.lock.withLockVoid { self._defaultCallOptions = newValue } }
  }
  public var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? {
    get { self.lock.withLock { return self._interceptors } }
    set { self.lock.withLockVoid { self._interceptors = newValue } }
  }

  /// Creates a client for the control_center.ImportantInfoService service.
  ///
  /// - Parameters:
  ///   - channel: `GRPCChannel` to the service host.
  ///   - defaultCallOptions: Options to use for each service call if the user doesn't provide them.
  ///   - interceptors: A factory providing interceptors for each RPC.
  public init(
    channel: GRPCChannel,
    defaultCallOptions: CallOptions = CallOptions(),
    interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? = nil
  ) {
    self.channel = channel
    self._defaultCallOptions = defaultCallOptions
    self._interceptors = interceptors
  }
}

public struct ControlCenter_ImportantInfoServiceNIOClient: ControlCenter_ImportantInfoServiceClientProtocol {
  public var channel: GRPCChannel
  public var defaultCallOptions: CallOptions
  public var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol?

  /// Creates a client for the control_center.ImportantInfoService service.
  ///
  /// - Parameters:
  ///   - channel: `GRPCChannel` to the service host.
  ///   - defaultCallOptions: Options to use for each service call if the user doesn't provide them.
  ///   - interceptors: A factory providing interceptors for each RPC.
  public init(
    channel: GRPCChannel,
    defaultCallOptions: CallOptions = CallOptions(),
    interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? = nil
  ) {
    self.channel = channel
    self.defaultCallOptions = defaultCallOptions
    self.interceptors = interceptors
  }
}

@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
public protocol ControlCenter_ImportantInfoServiceAsyncClientProtocol: GRPCClient {
  static var serviceDescriptor: GRPCServiceDescriptor { get }
  var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? { get }

  func makeForceRefreshHomepageInfoCacheCall(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions?
  ) -> GRPCAsyncUnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>

  func makeGetHomepageInfosCall(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions?
  ) -> GRPCAsyncUnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>
}

@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
extension ControlCenter_ImportantInfoServiceAsyncClientProtocol {
  public static var serviceDescriptor: GRPCServiceDescriptor {
    return ControlCenter_ImportantInfoServiceClientMetadata.serviceDescriptor
  }

  public var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? {
    return nil
  }

  public func makeForceRefreshHomepageInfoCacheCall(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) -> GRPCAsyncUnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse> {
    return self.makeAsyncUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.forceRefreshHomepageInfoCache.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeForceRefreshHomepageInfoCacheInterceptors() ?? []
    )
  }

  public func makeGetHomepageInfosCall(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) -> GRPCAsyncUnaryCall<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse> {
    return self.makeAsyncUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.getHomepageInfos.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeGetHomepageInfosInterceptors() ?? []
    )
  }
}

@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
extension ControlCenter_ImportantInfoServiceAsyncClientProtocol {
  public func forceRefreshHomepageInfoCache(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) async throws -> ControlCenter_HomepageResponse {
    return try await self.performAsyncUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.forceRefreshHomepageInfoCache.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeForceRefreshHomepageInfoCacheInterceptors() ?? []
    )
  }

  public func getHomepageInfos(
    _ request: SwiftProtobuf.Google_Protobuf_Empty,
    callOptions: CallOptions? = nil
  ) async throws -> ControlCenter_HomepageResponse {
    return try await self.performAsyncUnaryCall(
      path: ControlCenter_ImportantInfoServiceClientMetadata.Methods.getHomepageInfos.path,
      request: request,
      callOptions: callOptions ?? self.defaultCallOptions,
      interceptors: self.interceptors?.makeGetHomepageInfosInterceptors() ?? []
    )
  }
}

@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
public struct ControlCenter_ImportantInfoServiceAsyncClient: ControlCenter_ImportantInfoServiceAsyncClientProtocol {
  public var channel: GRPCChannel
  public var defaultCallOptions: CallOptions
  public var interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol?

  public init(
    channel: GRPCChannel,
    defaultCallOptions: CallOptions = CallOptions(),
    interceptors: ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol? = nil
  ) {
    self.channel = channel
    self.defaultCallOptions = defaultCallOptions
    self.interceptors = interceptors
  }
}

public protocol ControlCenter_ImportantInfoServiceClientInterceptorFactoryProtocol: Sendable {

  /// - Returns: Interceptors to use when invoking 'forceRefreshHomepageInfoCache'.
  func makeForceRefreshHomepageInfoCacheInterceptors() -> [ClientInterceptor<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>]

  /// - Returns: Interceptors to use when invoking 'getHomepageInfos'.
  func makeGetHomepageInfosInterceptors() -> [ClientInterceptor<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>]
}

public enum ControlCenter_ImportantInfoServiceClientMetadata {
  public static let serviceDescriptor = GRPCServiceDescriptor(
    name: "ImportantInfoService",
    fullName: "control_center.ImportantInfoService",
    methods: [
      ControlCenter_ImportantInfoServiceClientMetadata.Methods.forceRefreshHomepageInfoCache,
      ControlCenter_ImportantInfoServiceClientMetadata.Methods.getHomepageInfos,
    ]
  )

  public enum Methods {
    public static let forceRefreshHomepageInfoCache = GRPCMethodDescriptor(
      name: "ForceRefreshHomepageInfoCache",
      path: "/control_center.ImportantInfoService/ForceRefreshHomepageInfoCache",
      type: GRPCCallType.unary
    )

    public static let getHomepageInfos = GRPCMethodDescriptor(
      name: "GetHomepageInfos",
      path: "/control_center.ImportantInfoService/GetHomepageInfos",
      type: GRPCCallType.unary
    )
  }
}

/// To build a server, implement a class that conforms to this protocol.
public protocol ControlCenter_ImportantInfoServiceProvider: CallHandlerProvider {
  var interceptors: ControlCenter_ImportantInfoServiceServerInterceptorFactoryProtocol? { get }

  /// 强制刷新首页信息缓存
  func forceRefreshHomepageInfoCache(request: SwiftProtobuf.Google_Protobuf_Empty, context: StatusOnlyCallContext) -> EventLoopFuture<ControlCenter_HomepageResponse>

  /// 获取首页信息
  func getHomepageInfos(request: SwiftProtobuf.Google_Protobuf_Empty, context: StatusOnlyCallContext) -> EventLoopFuture<ControlCenter_HomepageResponse>
}

extension ControlCenter_ImportantInfoServiceProvider {
  public var serviceName: Substring {
    return ControlCenter_ImportantInfoServiceServerMetadata.serviceDescriptor.fullName[...]
  }

  /// Determines, calls and returns the appropriate request handler, depending on the request's method.
  /// Returns nil for methods not handled by this service.
  public func handle(
    method name: Substring,
    context: CallHandlerContext
  ) -> GRPCServerHandlerProtocol? {
    switch name {
    case "ForceRefreshHomepageInfoCache":
      return UnaryServerHandler(
        context: context,
        requestDeserializer: ProtobufDeserializer<SwiftProtobuf.Google_Protobuf_Empty>(),
        responseSerializer: ProtobufSerializer<ControlCenter_HomepageResponse>(),
        interceptors: self.interceptors?.makeForceRefreshHomepageInfoCacheInterceptors() ?? [],
        userFunction: self.forceRefreshHomepageInfoCache(request:context:)
      )

    case "GetHomepageInfos":
      return UnaryServerHandler(
        context: context,
        requestDeserializer: ProtobufDeserializer<SwiftProtobuf.Google_Protobuf_Empty>(),
        responseSerializer: ProtobufSerializer<ControlCenter_HomepageResponse>(),
        interceptors: self.interceptors?.makeGetHomepageInfosInterceptors() ?? [],
        userFunction: self.getHomepageInfos(request:context:)
      )

    default:
      return nil
    }
  }
}

/// To implement a server, implement an object which conforms to this protocol.
@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
public protocol ControlCenter_ImportantInfoServiceAsyncProvider: CallHandlerProvider, Sendable {
  static var serviceDescriptor: GRPCServiceDescriptor { get }
  var interceptors: ControlCenter_ImportantInfoServiceServerInterceptorFactoryProtocol? { get }

  /// 强制刷新首页信息缓存
  func forceRefreshHomepageInfoCache(
    request: SwiftProtobuf.Google_Protobuf_Empty,
    context: GRPCAsyncServerCallContext
  ) async throws -> ControlCenter_HomepageResponse

  /// 获取首页信息
  func getHomepageInfos(
    request: SwiftProtobuf.Google_Protobuf_Empty,
    context: GRPCAsyncServerCallContext
  ) async throws -> ControlCenter_HomepageResponse
}

@available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
extension ControlCenter_ImportantInfoServiceAsyncProvider {
  public static var serviceDescriptor: GRPCServiceDescriptor {
    return ControlCenter_ImportantInfoServiceServerMetadata.serviceDescriptor
  }

  public var serviceName: Substring {
    return ControlCenter_ImportantInfoServiceServerMetadata.serviceDescriptor.fullName[...]
  }

  public var interceptors: ControlCenter_ImportantInfoServiceServerInterceptorFactoryProtocol? {
    return nil
  }

  public func handle(
    method name: Substring,
    context: CallHandlerContext
  ) -> GRPCServerHandlerProtocol? {
    switch name {
    case "ForceRefreshHomepageInfoCache":
      return GRPCAsyncServerHandler(
        context: context,
        requestDeserializer: ProtobufDeserializer<SwiftProtobuf.Google_Protobuf_Empty>(),
        responseSerializer: ProtobufSerializer<ControlCenter_HomepageResponse>(),
        interceptors: self.interceptors?.makeForceRefreshHomepageInfoCacheInterceptors() ?? [],
        wrapping: { try await self.forceRefreshHomepageInfoCache(request: $0, context: $1) }
      )

    case "GetHomepageInfos":
      return GRPCAsyncServerHandler(
        context: context,
        requestDeserializer: ProtobufDeserializer<SwiftProtobuf.Google_Protobuf_Empty>(),
        responseSerializer: ProtobufSerializer<ControlCenter_HomepageResponse>(),
        interceptors: self.interceptors?.makeGetHomepageInfosInterceptors() ?? [],
        wrapping: { try await self.getHomepageInfos(request: $0, context: $1) }
      )

    default:
      return nil
    }
  }
}

public protocol ControlCenter_ImportantInfoServiceServerInterceptorFactoryProtocol: Sendable {

  /// - Returns: Interceptors to use when handling 'forceRefreshHomepageInfoCache'.
  ///   Defaults to calling `self.makeInterceptors()`.
  func makeForceRefreshHomepageInfoCacheInterceptors() -> [ServerInterceptor<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>]

  /// - Returns: Interceptors to use when handling 'getHomepageInfos'.
  ///   Defaults to calling `self.makeInterceptors()`.
  func makeGetHomepageInfosInterceptors() -> [ServerInterceptor<SwiftProtobuf.Google_Protobuf_Empty, ControlCenter_HomepageResponse>]
}

public enum ControlCenter_ImportantInfoServiceServerMetadata {
  public static let serviceDescriptor = GRPCServiceDescriptor(
    name: "ImportantInfoService",
    fullName: "control_center.ImportantInfoService",
    methods: [
      ControlCenter_ImportantInfoServiceServerMetadata.Methods.forceRefreshHomepageInfoCache,
      ControlCenter_ImportantInfoServiceServerMetadata.Methods.getHomepageInfos,
    ]
  )

  public enum Methods {
    public static let forceRefreshHomepageInfoCache = GRPCMethodDescriptor(
      name: "ForceRefreshHomepageInfoCache",
      path: "/control_center.ImportantInfoService/ForceRefreshHomepageInfoCache",
      type: GRPCCallType.unary
    )

    public static let getHomepageInfos = GRPCMethodDescriptor(
      name: "GetHomepageInfos",
      path: "/control_center.ImportantInfoService/GetHomepageInfos",
      type: GRPCCallType.unary
    )
  }
}